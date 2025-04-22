import sys
import tkinter as tk
from pathlib import Path
from tkinter import Tk, ttk

from mvrgx.project import VERSION


def run_gui(mv_workdir: str | Path | None = None) -> int | None:
    window = Tk()
    window.title(f'mvrgx {VERSION} GUI')
    window.geometry('800x400+200+200')
    ttk.Label(window, text=f'mvrgx {VERSION} GUI').pack()

    mv_workdir = Path(mv_workdir) if mv_workdir is not None else Path('.')

    tkframe_cwd_list = ttk.Frame(window)
    tkframe_cwd_list.pack()
    full_glob: list[Path] = sorted([*mv_workdir.glob('*')], key=lambda fp: fp.is_file())
    for f in full_glob:
        ttk.Label(window, text=f.name + ('/' if f.is_dir() else '')).pack()

    window.mainloop()

if __name__ == '__main__':
    sys.exit(run_gui())
