from collections.abc import Callable
from pathlib import Path

import mutagen
from mutagen import flac, mp3

from mvrgx.logging import logger


class FileMeta:
    def __init__(self, fp: str | Path):
        self.stat = Path(fp).stat()
        self.path = Path(fp).absolute()

        self.name: str = self.path.name
        self.stem: str = self.path.stem
        self.suffix: str = self.path.suffix.strip('.')
        self.bytes: int = self.stat.st_size
        self.kb: float = round(self.bytes / 1000, 4)
        self.mb: float = round(self.kb / 1000, 4)
        self.gb: float = round(self.mb / 1000, 4)
        self.ctime: float = self.stat.st_ctime
        self.atime: float = self.stat.st_atime
        self.mtime: float = self.stat.st_mtime

    def __repr__(self) -> str:
        return f'FileMeta(path={self.path}, bytes={self.bytes})'

def empty_on_key_index_fail(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (KeyError, IndexError) as e:
            logger.debug(f'Metadata retrieval failed, returning empty string ({e.__class__.__name__}: {e})')
            return ''
    return wrapper

class AudioMeta:
    INFO_CLS: dict[str, Callable[[str], mutagen.FileType]] = { # type: ignore
        'flac': flac.FLAC,
        'mp3': mp3.MP3,
    }

    def __init__(self, fp: str | Path):
        self.fp: Path = Path(fp)
        self.ftype: str = self.fp.suffix.strip('.')
        self.meta: mutagen.FileType = self.INFO_CLS[self.ftype](self.fp) # type: ignore

    def __repr__(self) -> str:
        return f'AudioMeta(ftype={self.ftype!r}, {', '.join(
            f'{k}={getattr(self, k)!r}' for k in ('title', 'artist', 'album', 'albumartist', 'date', 'trackno')
        )})'

    @property
    @empty_on_key_index_fail
    def title(self) -> str:
        match self.ftype:
            case 'flac': return self.meta['title'][0]
            case 'mp3': return self.meta['TIT2'].text[0]
            case _: raise ValueError(f'Unhandled type: {self.ftype}')

    @property
    @empty_on_key_index_fail
    def artist(self) -> str:
        match self.ftype:
            case 'flac': return self.meta['artist'][0]
            case 'mp3': return self.meta['TPE1'].text[0]
            case _: raise ValueError(f'Unhandled type: {self.ftype}')

    @property
    @empty_on_key_index_fail
    def album(self) -> str:
        match self.ftype:
            case 'flac': return self.meta['album'][0]
            case 'mp3': return self.meta['TALB'].text[0]
            case _: raise ValueError(f'Unhandled type: {self.ftype}')

    @property
    @empty_on_key_index_fail
    def albumartist(self) -> str:
        match self.ftype:
            case 'flac': return self.meta['albumartist'][0]
            case 'mp3': return self.meta['TPE2'].text[0]
            case _: raise ValueError(f'Unhandled type: {self.ftype}')

    @property
    @empty_on_key_index_fail
    def date(self) -> str:
        match self.ftype:
            case 'flac': return self.meta['date'][0]
            case 'mp3': return str(self.meta['TDRC'].text[0])
            case _: raise ValueError(f'Unhandled type: {self.ftype}')

    @property
    @empty_on_key_index_fail
    def trackno(self) -> str:
        match self.ftype:
            case 'flac': return self.meta['tracknumber'][0]
            case 'mp3': return self.meta['TRCK'].text[0]
            case _: raise ValueError(f'Unhandled type: {self.ftype}')
