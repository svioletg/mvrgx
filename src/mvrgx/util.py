import re
from collections.abc import Callable
from pathlib import Path

import colorama
from colorama import Back, Fore, Style

colorama.init(autoreset=True)

def highlight_regex(match: re.Match[str], color: str) -> str:
    if not color.startswith('\x1b'):
        fg, *bg = color.split(' on ')
        fg = getattr(Fore, fg.upper())
        if len(bg) > 0:
            color = fg + getattr(Back, bg[0].upper())
        else:
            color = fg
    ret: list[str] = list(match.string)
    ret.insert(match.start(), color)
    ret.insert(match.end() + 1, Style.RESET_ALL)
    return ''.join(ret)

def string_diff(s1: str, s2: str) -> str:
    for n, (a, b) in enumerate(zip(s1, s2)):
        if a != b:
            return s2[n:]
    return ''

def glob_sep(
        src: Path,
        pattern: str,
        *,
        recurs: bool = False,
        flt: Callable[[Path], bool] | None = None,
        sort: bool | Callable = False,
        sort_reverse: bool = False
    ) -> tuple[list[Path], list[Path]]:
    """
    `glob`s a directory with the given pattern, separating into two different lists of directories and files,
    optionally sorting them, and returning them as a tuple.

    :param sort: If `True`, default sort is used. If `False`, no sorting is done.
        If given a function, the lists will be sorted according to that key.
    :param sort_reverse: Whether to sort the lists in reverse. Only used if `sort` is not `False`.
    :param flt: A filter function to call on each path, only including paths where `flt(path)` is `True`.
        If `None`, no filtering is done.
    """
    globbed_dirs: list[Path] = []
    globbed_files: list[Path] = []
    for f in (src.rglob if recurs else src.glob)(pattern):
        if (flt is not None) and (flt(f) is False):
            continue
        (globbed_dirs if f.is_dir() else globbed_files).append(f)

    if sort is not False:
        sort_key: None | Callable = None if sort is True else sort
        globbed_dirs.sort(key=sort_key, reverse=sort_reverse)
        globbed_files.sort(key=sort_key, reverse=sort_reverse)

    return globbed_dirs, globbed_files
