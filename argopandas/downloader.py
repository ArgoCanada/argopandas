
"""
This module exposes :func:`download_one`, :func:`download_sequential`,
and :func:`download_async` for efficiently downloading large and/or
numerous files from Argo mirrors. Many of the problems it solves are
better handled by the urllib3 package, which may replace this module
in the future.
"""

import os
import urllib.request
from urllib.error import URLError
from http.client import InvalidURL
from concurrent.futures import ThreadPoolExecutor, as_completed
from .progress import guess_progressor


def _common_prefix(urls):
    if not urls:
        return ''
    max_length = max(len(url) for url in urls)

    # probably faster to use a recursive splitting strategy
    for i in reversed(range(1, max_length + 1)):
        prefix = urls[0][:i]
        if all(url[:i] == prefix for url in urls):
            return prefix

    return ''


def _init_message(urls):
    if not urls:
        return None
    elif len(urls) == 1:
        return f"Downloading '{urls[0]}'"

    common = _common_prefix([os.path.dirname(url) for url in urls])
    if common:
        return f"Downloading {len(urls)} files from '{common}'"
    else:
        return f"Downloading {len(urls)} files"


def download_one(url, dest_file, quiet=False):
    """
    Downloads one file with an optional progress bar.

    :param url: A url from which to download. This can be any
        url supported by ``urllib.request.urlopen()``.
    :param dest_file: A filename to which the file should be
        downloaded. The file is actually downloaded to
        ``dest_file + '.argotemp`` and renamed to ``dest_file``.
        The containing folder is created if it does not exist.
        upon successful and complete download.
    :param quiet: Use ``True`` to suppress progress updates.

    :raises InvalidURL: on malformed ``url`` argument
    :raises URLError: on error whilst downloading
    :raises IOError: on disk IO error
    """
    dir_name = os.path.dirname(dest_file)
    if dir_name:
        os.makedirs(dir_name, exist_ok=True)

    # like curl_download in R, do download to a tempfile
    # in the same directory to avoid writing a corrupt
    # file to dest_file (rename or delete it afterward)
    dest_file_temp = dest_file + '.argotmp'

    # used for status updates
    message = _init_message([url])

    try:
        with urllib.request.urlopen(url) as src:
            file_len = src.headers['Content-Length']
            if file_len and not quiet:
                pb = guess_progressor(int(file_len), init_message=message, quiet=quiet)
            else:
                pb = guess_progressor(1, quiet=quiet)

            with pb, open(dest_file_temp, 'wb') as dst:
                block_size = 8192
                while True:
                    buffer = src.read(block_size)
                    if not buffer:
                        break
                    dst.write(buffer)
                    pb.bump(len(buffer))

            if not file_len:
                pb.bump(1)  # pragma: no cover

            if os.path.exists(dest_file):
                os.unlink(dest_file)
            os.rename(dest_file_temp, dest_file)
    finally:
        if os.path.exists(dest_file_temp):
            os.unlink(dest_file_temp)  # pragma: no cover


def download_one_noexcept(url, dest_file, quiet=False):
    """
    A version of :func:`download_one` that returns an error
    message (or ``None`` if there was no error) instead of
    raising an exception.
    """
    try:
        download_one(url, dest_file, quiet=quiet)
    except (URLError, InvalidURL, FileNotFoundError) as e:
        return str(e)


def download_sequential(files, quiet=False, max_errors=50):
    """
    Downloads an iterable of url, dest_file tuples with optional progress
    bar. This is designed to produce reasonable output for the use case
    where many files are being downloaded with a reasonable chance
    of failure (e.g., from a slow FTP server). It tries to download
    as many files as possible before failing.

    :param files: An iterable of ``(url, dest_file)`` (see :func:`download_one`)
    :param quiet: Use ``True`` to suppress progress updates
    :param max_errors: The maximum number of errors to accumulate before
        aborting the entire operation.

    :return: A list of tuples in the form ``(i: int, error: str)`` describing
        errors that occured whilst downloading ``files``.
    """

    files = list(files)
    errors = []

    if not files:
        return []

    # for one file we can display a progress bar of the bytes
    # which is useful for large files such as the index
    if len(files) == 1:
        url, dest_file = files[0]
        err = download_one_noexcept(url, dest_file, quiet=quiet)
        if err:
            errors.append((0, err))
        return errors

    message = _init_message([item[0] for item in files])
    pb = guess_progressor(len(files), quiet=quiet, init_message=message)
    with pb:
        for i, urldest in enumerate(files):
            url, dest_file = urldest
            pb.bump(0, message=os.path.basename(url))
            err = download_one_noexcept(url, dest_file, quiet=True)
            if err:
                errors.append((i, err))
            pb.bump(1)
            if len(errors) >= max_errors:
                break

    return errors


def download_async(files, quiet=False, max_workers=6, max_errors=50):
    """
    Uses a ``concurrent.futures.ThreadPoolExecutor`` to download
    files using ``max_worker`` threads instead of sequentially
    like :func:`download_sequential`. When downloading many files
    (like Argo NetCDF files) this is usually much faster.
    """
    files = list(files)
    if len(files) <= 1 or max_workers <= 1:
        return download_sequential(files, quiet=quiet)

    message = _init_message([item[0] for item in files])
    pb = guess_progressor(len(files), quiet=quiet, init_message=message)
    with pb, ThreadPoolExecutor(max_workers=max_workers) as executor:
        future_map = {}
        for i, urldest in enumerate(files):
            url, dest_file = urldest
            future = executor.submit(download_one_noexcept, url, dest_file, True)
            future_map[future] = (i, url, dest_file)

        errors = []
        for future in as_completed(future_map):
            i, url, dest_file = future_map[future]
            pb.bump(1, message=os.path.basename(url))
            err = future.result()
            if err:
                errors.append((i, err))
            if len(errors) >= max_errors:
                break

        return errors
