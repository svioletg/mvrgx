import re
from argparse import ArgumentParser
from collections.abc import Callable
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import colorama
from colorama import Back, Fore, Style

colorama.init(autoreset=True)

@dataclass
class CliArg:
    """
    A "pre-packaged" command-line argument, mainly used for parity between the CLI and GUI argument sets.

    :param name: A tuple of one or two strings; short or long alone, or both short and long names.
    """
    name: tuple[str] | tuple[str, str]
    kwargs: dict[str, Any]

    def add_to(self, parser: ArgumentParser, overrides: dict[str, Any] | None = None):
        parser.add_argument(*self.name, **self.kwargs | (overrides or {}))

CLARG_LOG_LEVEL: CliArg = CliArg(
    ('-log', '--log-level'),
    {
        'type': lambda s: s.upper(),
        'choices': ('DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRTIICAL'),
        'default': 'INFO',
        'help': 'Sets the log level.'
    }
)

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
        sort_reverse: bool = False,
        limit: int = 10_000,
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
    n: int = 0
    for f in (src.rglob if recurs else src.glob)(pattern):
        if (flt is not None) and (flt(f) is False):
            continue
        if n > limit:
            raise ValueError(f'Search limit exceeded ({limit})')
        (globbed_dirs if f.is_dir() else globbed_files).append(f)
        n += 1
    if sort is not False:
        sort_key: None | Callable = None if sort is True else sort
        globbed_dirs.sort(key=sort_key, reverse=sort_reverse)
        globbed_files.sort(key=sort_key, reverse=sort_reverse)

    return globbed_dirs, globbed_files

def closest_existing_dir(fp: Path) -> Path | None:
    """Find the closest existing dir in a path, returning None if no more parents are left to search."""
    if fp.is_dir():
        return fp
    if len(fp.parts) == 1:
        return None
    return closest_existing_dir(fp.parent)
