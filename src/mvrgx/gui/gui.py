import re
import sys
import time
from collections.abc import Generator
from pathlib import Path
from pprint import pprint
from typing import Any, Protocol, Self

from PySide6.QtWidgets import QApplication, QDialog, QFileDialog, QListWidget, QListWidgetItem, QMainWindow

from mvrgx.core import NUM_GROUP_RGX, parse_output_pattern
from mvrgx.gui.ui_dialog_ok import Ui_DialogOK
from mvrgx.gui.ui_dialog_task import Ui_DialogTask
from mvrgx.gui.ui_dialog_yesno import Ui_DialogYN
from mvrgx.gui.ui_main import Ui_MainWindow
from mvrgx.logging import enable_logging, logger
from mvrgx.project import PROJECT_ROOT, VERSION
from mvrgx.util import glob_sep

STYLE_PATH: Path = PROJECT_ROOT / 'gui/asset/qstyle.css'

STYLE_VAR_DEF_RGX: re.Pattern[str] = re.compile(r"(--.+?): (.+);")
STYLE_VAR_ACCESS_RGX: re.Pattern[str] = re.compile(r"var\((.+)\)")

def listWidget_iter(widget: QListWidget) -> Generator[QListWidgetItem, None, None]:
    for n in range(widget.count()):
        yield widget.item(n)

class DialogOK(QDialog):
    def __init__(self, style_sheet: str = ''):
        super().__init__()
        self.ui = Ui_DialogOK()
        self.ui.setupUi(self)
        self.setStyleSheet(style_sheet)
        self.style_sheet = style_sheet

class DialogYN(QDialog):
    def __init__(self, style_sheet: str = ''):
        super().__init__()
        self.ui = Ui_DialogYN()
        self.ui.setupUi(self)
        self.setStyleSheet(style_sheet)
        self.style_sheet = style_sheet

class DialogTask(QDialog):
    def __init__(self, style_sheet: str = ''):
        super().__init__()
        self.ui = Ui_DialogTask()
        self.ui.setupUi(self)
        self.setStyleSheet(style_sheet)
        self.style_sheet = style_sheet

        self.ui.progressBar.setValue(0)

def spawn_dialog[T: Any](cls: type[T], title: str, body: str, *, modal: bool = True, **cls_kwargs) -> tuple[T, int]:
    """
    Spawn a dialog box with a given title and message (body), returning the instanced object and its exit code.
    """
    inst = cls(**cls_kwargs)
    inst.setWindowTitle(title)
    inst.ui.labelMessage.setText(body)
    ret = inst.exec() if modal else inst.open()
    return inst, ret

class MainWindow(QMainWindow):
    def __init__(self, style_sheet: str = ''):
        logger.info('Initializing main UI...')
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setStyleSheet(style_sheet)
        self.style_sheet = style_sheet
        self.setWindowTitle(f'mvrgx v{VERSION}')

        # Signals
        logger.info('Connecting signals...')
        self.ui.pushButtonSrcBrowse.clicked.connect(self._ask_src_dir)

        self.ui.lineEditSrcDir.setText(str(Path('.').resolve()))
        self.ui.lineEditSrcDir.editingFinished.connect(self._update_src_dir_preview)
        self.ui.lineEditSrcDir.textChanged.connect(self._validate_src_dir)
        self.ui.lineEditSrcDir.editingFinished.emit()

        self.ui.labelSrcDirErrMsg.setVisible(False)

        self.ui.listWidgetSrcContents.itemDoubleClicked.connect(self._append_to_src_dir)

        self.ui.lineEditInputRegex.editingFinished.connect(self._update_mv_preview)
        self.ui.lineEditInputRegex.editingFinished.emit()

        self.ui.lineEditOutputPattern.textChanged.connect(self._validate_output_pattern)
        self.ui.lineEditOutputPattern.editingFinished.connect(self._update_mv_preview)
        self.ui.lineEditOutputPattern.editingFinished.emit()

        self.ui.pushButtonRenameFiles.clicked.connect(self._rename_files_clicked)

        logger.info('UI init complete')

    @property
    def src_dir(self) -> Path:
        return Path(self.ui.lineEditSrcDir.text()).resolve()

    @property
    def input_regex(self) -> re.Pattern[str]:
        return re.compile(self.ui.lineEditInputRegex.text())

    @property
    def output_pattern(self) -> str:
        return self.ui.lineEditOutputPattern.text()

    @property
    def recurs_search(self) -> bool:
        return self.ui.checkBoxRecursive.isChecked()

    def _validate_src_dir(self):
        self.ui.labelSrcDirErrMsg.setVisible(not Path(self.ui.lineEditSrcDir.text()).is_dir())

    def _validate_output_pattern(self):
        msg: str = ''
        num_groups: list[int] = [*map(lambda i: int(i.strip('\\')), NUM_GROUP_RGX.findall(self.output_pattern))]
        if not self.output_pattern:
            msg = 'Cannot be empty'
        elif len(num_groups) == 0:
            msg = 'Must contain at least one replacement group'
        elif any(n < 1 for n in num_groups):
            msg = 'Group index cannot be less than 1'
        elif num_groups[-1] > self.input_regex.groups:
            msg = 'Group index cannot be greater than the total number of groups' \
                  + f' ({self.input_regex.groups})'
        self.ui.labelOutputPatternWarning.setToolTip(msg)
        self.ui.labelOutputPatternWarning.setVisible(msg != '')
        self.ui.pushButtonRenameFiles.setEnabled(msg == '')

        if msg == '':
            self.ui.lineEditOutputPattern.setProperty('inputValid', 'True')
            self.refresh_style()
        else:
            self.ui.lineEditOutputPattern.setProperty('inputValid', 'False')
            self.refresh_style()

    def _ask_src_dir(self):
        dlg = QFileDialog(self, directory=str(self.src_dir if self.src_dir.is_dir() else '.'))
        dlg.setWindowTitle('Choose source directory...')
        dlg.setFileMode(dlg.FileMode.Directory)

        if dlg.exec():
            result: list[str] = dlg.selectedFiles()
            self.ui.lineEditSrcDir.setText(str(Path(result[0]).resolve()))
            self.ui.lineEditSrcDir.editingFinished.emit()

    def _update_src_dir_preview(self):
        self.ui.listWidgetSrcContents.clear()

        if not self.src_dir.is_dir():
            self.ui.labelSrcDirCount.setText('Directory empty.')
            return

        try:
            contents_dirs, contents_files = glob_sep(self.src_dir, '*', sort=True)
        except ValueError as e:
            # DialogOK.spawn('Error', str(e), style_sheet=self.style_sheet)
            x,y=spawn_dialog(Ui_DialogOK, 'Error', str(e), style_sheet=self.style_sheet)
            return

        contents: list[Path] = [Path('../')] + contents_dirs + contents_files
        if len(contents) - 1 == 0:
            self.ui.labelSrcDirCount.setText('Directory empty.')
        else:
            self.ui.labelSrcDirCount.setText(f'{len(contents) - 1} item(s) total.')

        for f in contents:
            item = QListWidgetItem()
            item.setText(str(f.name) + ('/' if f.is_dir() else ''))
            self.ui.listWidgetSrcContents.addItem(item)

    def _append_to_src_dir(self, item: QListWidgetItem):
        new_path: Path = Path(self.src_dir, item.text()).resolve()
        if not new_path.is_dir():
            return
        self.ui.lineEditSrcDir.setText(str(new_path))
        self.ui.lineEditSrcDir.editingFinished.emit()

    def _update_mv_preview(self):
        self._validate_output_pattern()
        self.ui.listWidgetMvBefore.clear()
        self.ui.listWidgetMvAfter.clear()

        if not self.src_dir.is_dir():
            return

        try:
            contents_dirs, contents_files = glob_sep(self.src_dir, '*', recurs=self.recurs_search)
        except ValueError as e:
            spawn_dialog(DialogOK, 'Error', str(e), style_sheet=self.style_sheet)
            return

        matched_dirs: list[re.Match[str]] = sorted([
            m for f in contents_dirs \
            if (m := self.input_regex.search(str(f.relative_to(self.src_dir))))
        ], key=lambda i: i.string)

        matched_files: list[re.Match[str]] = sorted([
            m for f in contents_files \
            if (m := self.input_regex.search(str(f.relative_to(self.src_dir))))
        ], key=lambda i: i.string)

        for m in matched_dirs + matched_files:
            item = QListWidgetItem()
            full_path: Path = self.src_dir / m.string
            item.setText(m.string + ('/' if full_path.is_dir() else ''))
            item.setToolTip(str(Path(m.string).resolve()))
            self.ui.listWidgetMvBefore.addItem(item)

        if self.output_pattern and (self.ui.labelOutputPatternWarning.toolTip() == ''):
            for m in matched_dirs + matched_files:
                item = QListWidgetItem()
                full_path: Path = self.src_dir / m.string
                try:
                    parsed: str = parse_output_pattern(self.output_pattern, m, full_path, warn_no_group=False)
                    item.setText(parsed + ('/' if full_path.is_dir() else ''))
                    item.setToolTip(str(Path(parsed).resolve()))
                except (AttributeError, ValueError) as e:
                    spawn_dialog(
                        DialogOK,
                        'Error parsing output pattern',
                        f'{e.__class__.__name__}: {e}',
                        style_sheet=self.style_sheet
                    )
                    break
                self.ui.listWidgetMvAfter.addItem(item)

    def _validate_output_paths(self) -> bool:
        out_paths: list[Path] = []
        final_parts: list[str] = []
        for n in range(self.ui.listWidgetMvAfter.count()):
            i: QListWidgetItem = self.ui.listWidgetMvAfter.item(n)
            fp = Path(i.toolTip())
            out_paths.append(fp)
            if (final := fp.parts[-1]) in final_parts:
                spawn_dialog(
                    DialogOK,
                    'Output path validation error',
                    'All paths must end in a unique filename.',
                    style_sheet=self.style_sheet
                )
                return False
            final_parts.append(final)

        return True

    def _rename_files_clicked(self):
        if not self._validate_output_paths():
            return
        _, ret = spawn_dialog(
            DialogYN,
            'Confirm renaming',
            f'About to rename/move {self.ui.listWidgetMvBefore.count()} files.\nContinue?',
            style_sheet=self.style_sheet
        )

        if ret == 0:
            return
        move_map: dict[Path, Path] = {}
        for a, b in zip(listWidget_iter(self.ui.listWidgetMvBefore), listWidget_iter(self.ui.listWidgetMvAfter)):
            move_map[Path(a.toolTip())] = Path(b.toolTip())
        print(move_map)

        dlg, _ = spawn_dialog(
            DialogTask,
            'Renaming...',
            '',
            modal=False,
            style_sheet=self.style_sheet
        )

        for n, (k, v) in enumerate(move_map.items()):
            print(n, k, v)
            time.sleep(0.5)
            i = QListWidgetItem()
            i.setText(f'{k}  ->  {v}')
            dlg.ui.listWidgetStatus.addItem(i)
            dlg.ui.labelMessage.setText(f'{n} of {len(move_map)} moved...')
            dlg.ui.progressBar.setValue(n // len(move_map))

    def refresh_style(self):
        self.setStyleSheet(self.style_sheet)

def parse_style_sheet(fp: str | Path) -> str:
    style_raw: str = Path(fp).read_text('utf-8')

    if (m := re.search(r":root {(.*?)}", style_raw, flags=re.S)) is None:
        style_root_inner: str = ''
        style_sheet: str = style_raw
    else:
        style_root_inner: str = str(m.groups(0)[0])
        style_sheet: str = style_raw[m.end(0):]

    style_vars: dict[str, str] = dict(STYLE_VAR_DEF_RGX.findall(style_root_inner))

    def _get_var(m: re.Match[str]) -> str:
        key: str = str(m.groups(0)[0])
        if key not in style_vars:
            logger.error(f'CSS var "{key}" is not defined in {Path(fp).relative_to(PROJECT_ROOT)}')
            return ''
        return style_vars[key]
    return STYLE_VAR_ACCESS_RGX.sub(_get_var, style_sheet)

def run_gui() -> int | None:
    enable_logging(logger, 'INFO')

    main_style: str = parse_style_sheet(STYLE_PATH)

    app = QApplication(sys.argv)

    window = MainWindow(main_style)
    window.show()

    logger.info('Executing...')
    return app.exec()

if __name__ == '__main__':
    sys.exit(run_gui())
