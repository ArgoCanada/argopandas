
import shutil
import sys


class Progressor:

    def __init__(self, total, start=0, init_message=None):
        self._value = start
        self._total = total
        self._init_message = init_message

    def bump(self, amount=1, message=None):
        self._value += amount
        self._update(self._value, self._total, message)
        return self._value, self._total

    def _initialize(self, value, total, message):
        pass

    def _update(self, value, total, message):
        pass

    def _finish(self, value, total):
        pass

    def __enter__(self):
        self._initialize(self._value, self._total, self._init_message)
        return self

    def __exit__(self, *execinfo):
        self._finish(self._value, self._total)


class SilentProgress(Progressor):
    def __init__(self, *args, **kwargs):
        super().__init__(0)


class ProgressBar(Progressor):

    def __init__(self, total, start=0, init_message=None,
                 width=None, file=None, interactive=None, message_len=30):
        super().__init__(total, start=start, init_message=init_message)

        if width is None:
            self._width = shutil.get_terminal_size().columns // 2 + message_len
        else:
            self._width = width

        if file is None:
            self._file = sys.stderr  # pragma: no cover
        else:
            self._file = file

        if interactive is None:
            self._interactive = self._check_is_interactive()  # pragma: no cover
        else:
            self._interactive = interactive

        # this bar is [====>    ] XX% message for interactive or ===== otherwise
        n_bar_chars = len('[] XXX% ')
        self._tick_width = max([self._width - message_len - n_bar_chars, 2])
        self._n_ticks = None
        self._message = None
        message_len = min([self._width - self._tick_width - n_bar_chars, message_len])
        self._messasge_len = max([message_len, 4])

    def _initialize(self, value, total, message):
        if message is not None:
            self._file.write(message)

        self._file.write('\n')

        if not self._interactive:
            self._file.write(f'[{" " * self._tick_width}]\n ')

        self._update(value, total, None)

    def _update(self, value, total, message):
        if value > total:
            err = f'Attempt to set ProgressBar value > total ({value}/{total}, {repr(message)})'
            raise RuntimeError(err)

        n_ticks = int(value / total * self._tick_width) if total != 0 else 0
        pct = value / total * 100 if total != 0 else 0

        is_fresh = self._n_ticks is None
        is_progressed = n_ticks != self._n_ticks
        new_message = message != self._message

        if is_fresh or is_progressed or new_message:
            if self._interactive:
                n_spaces = max([self._tick_width - n_ticks - 1, 0])
                ticks = '=' * n_ticks
                arrow = '>' if n_ticks != self._tick_width else ''
                spaces = ' ' * n_spaces
                pct_just = str(int(pct)).rjust(3)
                message = self._prepare_message(message)

                bar = f'\r[{ticks}{arrow}{spaces}] {pct_just}% {message}'
                self._file.write(bar)
            else:
                current_ticks = 0 if is_fresh else self._n_ticks
                self._file.write('=' * (n_ticks - current_ticks))

            self._n_ticks = n_ticks
            self._message = message

    def _finish(self, value, total):
        # if the bar finished, erase it! if it didn't
        # it's useful to see where progress stopped
        if self._interactive and value == total:
            self._file.write('\r' + (' ' * self._width) + '\r')
        else:
            self._file.write('\n')



    def _prepare_message(self, message):
        if message is None:
            return ''
        elif len(message) > self._messasge_len:
            return message[:(self._messasge_len - 3)] + '...'
        else:
            return message + ' ' * (self._messasge_len - len(message))


def _interactive():
    import __main__ as main
    return not hasattr(main, '__file__')


def guess_progressor(*args, quiet=False, **kwargs):
    if quiet or not _interactive():
        return SilentProgress()
    else:
        return ProgressBar(*args, **kwargs, interactive=True)  # pragma: no cover
