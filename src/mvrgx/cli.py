import os
import re
import shutil
import sys
import textwrap
from argparse import ArgumentParser
from pathlib import Path

import colorama
from colorama import Fore, Style
from tqdm import tqdm

from mvrgx.core import parse_output_pattern
from mvrgx.logging import enable_logging, logger
from mvrgx.util import CLARG_LOG_LEVEL

colorama.init(autoreset=True)

COLOR_PATH_OLD: str = Style.NORMAL + Fore.CYAN
COLOR_PATH_NEW: str = Fore.GREEN

def show_out_pattern_help():
    help_text: str = """
The output pattern accepts either numbered groups (\\1, \\2, \\3) or metadata-key groups (\\m:a{trackno}, \\m:f{suffix}).
Numbered groups will correspond to each group given for the input regex pattern, e.g. for the input pattern
'^(\\d+) - (.+)', and the output pattern 'Track \\1. \\2', \\1 will be replaced with what is captured by (\\d+),
and \\2 would be replaced with what is captured by (.+).

Metadata groups can be used to access file metadata in a similar replacement fashion. The syntax for a metadata
group is \\m:X{Y}, where X is the metadata category, and Y is the key name.
Supported metadata categories are: f (FILE / GENERAL), a (AUDIO).
FILE metadata contains things like the original file name, file suffix (last extension, minus the leading dot),
file size (in bytes, KB, MB, and GB), and so on. AUDIO metadata can be used for MP3 and FLAC files, and contains
information like track title, number, album, and artist.
"""
    print('\n\n'.join('    ' + '\n'.join(textwrap.wrap(p)).strip() for p in help_text.split('\n\n')))

arg_parser = ArgumentParser()
arg_parser.add_argument('regex', type=re.compile,
    help='Python-flavored regex pattern to match files against.' \
    + ' In bash, it is advised to give this pattern in single-quotes to avoid unexpected behavior.')
CLARG_LOG_LEVEL.add_to(arg_parser)
arg_parser.add_argument('-at', '--at-dir', type=Path, default=Path('.'),
    help='Path to run this search/replace from. Defaults to the current directory.')
arg_parser.add_argument('-o', '--out', type=str,
    help='Pattern to move/rename each file to.'
    + ' Use "\\N" to insert a capture group, where N is the index of the group.'
    + ' You can also access file metadata with the "\\m{...}" pattern. Use -o/--out :help for details.'
    + ' Omitting this option will instead print out files captured with the find pattern given,'
    + ' without making any changes.')
arg_parser.add_argument('-r', '--recursive', action='store_true',
    help='Searches this directory recursively. Default behavior is to only search the top level.')
arg_parser.add_argument('-p', '--preview', action='store_true',
    help='Displays the captured files and what their new names would be, and exits without modifying any files.')

def run_cli() -> int | None:
    args = arg_parser.parse_args()
    find_regex  : re.Pattern[str] = args.regex
    log_level   : str             = args.log_level
    root        : Path            = args.at_dir
    out_pattern : None | str      = args.out
    recurs      : bool            = args.recursive
    preview     : bool            = args.preview

    enable_logging(logger, log_level.upper())

    if out_pattern and (out_pattern.lower() == ':help'):
        show_out_pattern_help()
        return

    if not root.is_dir():
        logger.error(f'Not a directory or doesn\'t exist: {root}')

    full_glob: list[Path] = list((root.rglob('*') if recurs else root.glob('*')))
    matched: list[re.Match[str]] = [m for f in full_glob if (m := find_regex.search(str(f)))]

    if len(matched) == 0:
        print('No matches found.')
        return

    if out_pattern is None:
        print('\n'.join(str(Path(m.string)) for m in matched))
        print(f'\n{len(matched)} found.')
        return

    move_map: dict[Path, Path] = {}
    for fp_match in matched:
        orig_fp = Path(fp_match.string)
        move_map[orig_fp] = Path(*orig_fp.parts[:-1], parse_output_pattern(out_pattern, fp_match, orig_fp))

    preview_sep: str = '  ->  '
    max_preview_ln: int = max(sum(map(lambda i: len(str(i)), pair)) + len(preview_sep) for pair in move_map.items())
    if max_preview_ln > os.get_terminal_size().columns:
        for k, v in move_map.items():
            print(f'{COLOR_PATH_OLD}- {k}')
            print(f'{COLOR_PATH_NEW}+ {v}')
            # print(f'{COLOR_PATH_NEW}+ {('[...] ' + v.parts[-1]) if k.parts[:-1] == v.parts[:-1] else v}')
    else:
        for k, v in move_map.items():
            print(f'{COLOR_PATH_OLD}{k}{Style.RESET_ALL}'
                  + f'{preview_sep:>{max(len(str(i)) for i in move_map) + len(preview_sep) - len(str(k))}}'
                  + f'{COLOR_PATH_NEW}{v}')

    if preview:
        return

    print() # newline
    if (dupes := len(move_map.values()) - len(set(move_map.values()))) > 0:
        logger.warning(f'Output has {dupes} duplicate filenames;'
                       + ' if you continue, these files may be overwritten and lost')
    q = input(f'About to replace {len(move_map)} files. Continue? (y/n) ').strip().lower()
    if q != 'y':
        print('Aborting.')
        return

    for fp_from, fp_to in tqdm(move_map.items()):
        shutil.move(fp_from, fp_to)

if __name__ == '__main__':
    sys.exit(run_cli())
