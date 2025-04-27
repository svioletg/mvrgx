import re
from datetime import datetime
from pathlib import Path

from mvrgx.file_meta import AudioMeta, FileMeta
from mvrgx.logging import logger

NUM_GROUP_RGX: re.Pattern[str] = re.compile(r"(?<!\\)(\\\d+)")
META_KEY_RGX: re.Pattern[str] = re.compile(r"(\\m:([aA-zZ])\{(.+?)\})")

def parse_meta_key(fp: str | Path, s: str) -> str:
    fp = Path(fp)
    if (m := META_KEY_RGX.search(s)) is None:
        raise ValueError(f'Invalid metadata key format: {s!r}')
    _, mode, key = map(str, m.groups(0))
    key, *fmt = key.split(':')
    fmt = fmt[0] if fmt else None
    match mode:
        case 'f':
            info = FileMeta(fp)
        case 'a':
            if fp.suffix.strip('.') not in AudioMeta.INFO_CLS:
                return s
            info = AudioMeta(fp)
        case _:
            raise ValueError(f'Unrecognized metadata category: {mode}')
    return parse_formatter(str(getattr(info, key)), fmt)

def parse_formatter(s: str, fmt: str | None) -> str:
    if fmt is None:
        return s
    match fmt[0]:
        case 't':
            return datetime.fromtimestamp(float(s)).strftime(''.join(fmt[1:]))
        case 'z':
            return s.zfill(int(''.join(fmt[1:])))
        case _:
            raise ValueError(f'Unrecognized format char: {fmt[0]} (in: {fmt!r})')

def parse_output_pattern(
        out_pat: str,
        str_match: re.Match[str],
        full_path: Path,
        *,
        warn_no_group: bool = True
    ) -> str:
    repl_groups_num: set[str] = set(NUM_GROUP_RGX.findall(out_pat))
    repl_groups_meta: set[re.Match[str]] = set(META_KEY_RGX.finditer(out_pat))
    if len(repl_groups_num.union(repl_groups_meta)) == 0:
        if warn_no_group:
            logger.warning(f'Output pattern contains no valid groups: {out_pat!r}')

    new_str: str = out_pat
    for g in repl_groups_num:
        n: int = int(g.strip('\\'))
        new_str = new_str.replace(g, str(str_match.groups(0)[n - 1]))

    for g in repl_groups_meta:
        meta_key = str(g.groups(0)[0])
        new_str = new_str.replace(meta_key, parse_meta_key(full_path, meta_key))

    return new_str.replace('\\\\', '\\')
