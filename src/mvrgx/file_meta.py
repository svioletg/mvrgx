from collections.abc import Callable
from pathlib import Path

import mutagen
from mutagen import flac, mp3


class FileMeta:
    def __init__(self, fp: str | Path):
        self.stat = Path(fp).stat()

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
    def title(self) -> str:
        match self.ftype:
            case 'flac': return self.meta['title'][0]
            case 'mp3': return self.meta['TIT2'].text[0]
            case _: raise ValueError(f'Unhandled type: {self.ftype}')

    @property
    def artist(self) -> str:
        match self.ftype:
            case 'flac': return self.meta['artist'][0]
            case 'mp3': return self.meta['TPE1'].text[0]
            case _: raise ValueError(f'Unhandled type: {self.ftype}')

    @property
    def album(self) -> str:
        match self.ftype:
            case 'flac': return self.meta['album'][0]
            case 'mp3': return self.meta['TALB'].text[0]
            case _: raise ValueError(f'Unhandled type: {self.ftype}')

    @property
    def albumartist(self) -> str:
        match self.ftype:
            case 'flac': return self.meta['albumartist'][0]
            case 'mp3': return self.meta['TPE2'].text[0]
            case _: raise ValueError(f'Unhandled type: {self.ftype}')

    @property
    def date(self) -> str:
        match self.ftype:
            case 'flac': return self.meta['date'][0]
            case 'mp3': return str(self.meta['TDRC'].text[0])
            case _: raise ValueError(f'Unhandled type: {self.ftype}')

    @property
    def trackno(self) -> str:
        match self.ftype:
            case 'flac': return self.meta['tracknumber'][0]
            case 'mp3': return self.meta['TRCK'].text[0]
            case _: raise ValueError(f'Unhandled type: {self.ftype}')
