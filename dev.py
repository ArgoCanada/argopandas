
import argparse
import os
import sys
import shlex
import shutil
import re
from types import CodeType

def python(*args):
    command = sys.executable + ' ' + shlex.join(args)
    status = os.system(command)
    if status != 0:
        sys.stderr.write(f"{command} exited with status {status}")
        sys.exit(1)

def build_readme(args):
    parser = argparse.ArgumentParser(
        description='Build README.md from README.ipynb',
        usage=f"{os.path.basename(__file__)} build_readme [-h]"
    )
    parser.parse_args(args)

    # clean previous .md output
    if os.path.exists('README.md'):
        os.unlink('README.md')
    if os.path.exists('README_files'):
        shutil.rmtree('README_files')

    # generate .md for GitHub and PyPi
    python(
        '-m', 'jupyter', 'nbconvert', 'README.ipynb', '--execute',
        '--to',  'markdown', '--output', 'README.md'
    )

    # clean previous .rst output
    if os.path.exists('docs/README.rst'):
        os.unlink('docs/README.rst')
    if os.path.exists('docs/README_files'):
        shutil.rmtree('docs/README_files')

    # generate .rst for documentation
    python(
        '-m', 'jupyter', 'nbconvert', 'README.ipynb',
        '--to', 'rst', '--output', 'README.rst', '--output-dir', 'docs'
    )

    # apply some custom filters to README.md so that it shows up properly
    # on GitHub and PyPI
    content = None
    with open('README.md', 'rb') as f:
        content = f.read().decode('utf-8')

    # on Windows we get a lot of extraneous \r
    content = content.replace('\r', '')

    # pandas HTML is mostly ok except for the <style> blocks
    content = re.sub(r'<style.*?</style>', '', content, flags=re.MULTILINE | re.DOTALL)

    # rewrite README.md for GitHub
    with open('README.md', 'wb') as f:
        f.write(content.encode('utf-8'))

    # the landing page on PyPI doesn't host images, so remove any references
    # from the README. Could also upload a version in the future to a
    # github gist, for example, but this results in a totally fine
    # landing page on PyPI.
    content = re.sub(r'!\[png\]\(README_files/[^\n]*\n', '', content)

    # rewrite README_pypi.md for PyPI
    with open('README_pypi.md', 'wb') as f:
        f.write(content.encode('utf-8'))

    # do the same with .rst content
    content = None
    with open('docs/README.rst', 'rb') as f:
        content = f.read().decode('utf-8')

    # Windows generates extraneous \r that results in double linebreaks
    content = content.replace('\r', '')

    # any generated file path gets mangled on Windows; fix here
    content = content.replace('README_files%5C', 'README_files/')

    with open('docs/README.rst', 'wb') as f:
        f.write(content.encode('utf-8'))



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Python package development tools')
    parser.add_argument(
        'action', choices=['build_readme'],
        help='The subcommand name to execute'
    )

    args = parser.parse_args(sys.argv[1:2])
    if args.action == 'build_readme':
        build_readme(sys.argv[2:])
    else:
        raise RuntimeError(f"Unknown action: '{ args.action }'")
