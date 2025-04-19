import re

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
