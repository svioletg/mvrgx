import re
from pathlib import Path

from mvrgx.file_meta import AudioMeta, FileMeta
from mvrgx.logging import logger

META_KEY_RGX: re.Pattern = re.compile(r"(\\m:([aA-zZ])\{(\S+)\})")

def parse_meta_key(fp: str | Path, s: str) -> str:
    if (m := META_KEY_RGX.search(s)) is None:
        raise ValueError(f'Invalid metadata key format: {s!r}')
    _, mode, key = map(str, m.groups(0))
    match mode:
        case 'f':
            info = FileMeta(fp)
        case 'a':
            info = AudioMeta(fp)
        case _:
            raise ValueError(f'Unrecognized metadata category: {mode}')
    return getattr(info, key)

def parse_output_pattern(out_pat: str, fp_match: re.Match[str]) -> str:
    repl_groups_num: set[str] = set(re.findall(r"\\\d", out_pat))
    repl_groups_meta: set[re.Match[str]] = set(META_KEY_RGX.finditer(out_pat))
    if len(repl_groups_num.union(repl_groups_meta)) == 0:
        logger.warning('Output pattern contains no valid groups')

    # pprint(repl_groups_num)
    # pprint(repl_groups_meta)

    orig_fp = Path(fp_match.string)
    new_str: str = out_pat
    for g in repl_groups_num:
        n: int = int(g.strip('\\'))
        new_str = new_str.replace(g, str(fp_match.groups(0)[n]))
    for g in repl_groups_meta:
        meta_key = str(g.groups(0)[0])
        new_str = new_str.replace(meta_key, parse_meta_key(orig_fp, meta_key))

    return new_str
