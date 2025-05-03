import re
from argparse import ArgumentParser
from pathlib import Path
from typing import Literal

from mvrgx.cli import arg_parser as cli_args
from mvrgx.gui.gui import arg_parser as gui_args

ARGTABLE_RGX: re.Pattern[str] = re.compile(r"<!-- argtable:(\w+) -->")

def create_argtable(mode: str | Literal['cli', 'gui']) -> str:
    match mode:
        case 'cli':
            args = cli_args._actions
        case 'gui':
            args = gui_args._actions
        case _:
            raise ValueError(f'Unknown argtable mode: {mode}')

    table: list[str] = ['|Name|Description|', '|-|-|']
    table_row: str = '|{name}|{desc}|'

    for arg in args:
        name: str = ', '.join(f'`{i}`' for i in arg.option_strings) if arg.option_strings else f'`{arg.dest}`'
        desc: str = str(arg.help)
        table.append(table_row.format(name=name, desc=desc))

    return '\n'.join(table)

def parse(content: str) -> str:
    content = ARGTABLE_RGX.sub(lambda m: create_argtable(str(m.groups(0)[0])), content)
    return content

arg_parser = ArgumentParser()
arg_parser.add_argument('source', type=Path)
arg_parser.add_argument('-o', type=Path, dest='dest',
    help='Where to save the parsed markdown text. If ommitted, the text is printed out and not saved to disk.')

def main() -> int | None:
    args = arg_parser.parse_args()
    src  : Path        = args.source
    dest : None | Path = args.dest

    parsed_md: str = parse(src.read_text('utf-8'))

    if dest is None:
        print(parsed_md)
    else:
        dest.write_text(parsed_md, 'utf-8')
        print(f'Written to {dest.resolve()}')

if __name__ == '__main__':
    main()
