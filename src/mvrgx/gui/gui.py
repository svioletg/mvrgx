import re
import sys
from pathlib import Path

from PySide6.QtWidgets import QApplication, QDialog, QFileDialog, QListWidgetItem, QMainWindow

from mvrgx.core import NUM_GROUP_RGX, parse_output_pattern
from mvrgx.gui.ui_dialog_ok import Ui_DialogOK
from mvrgx.gui.ui_main import Ui_MainWindow
from mvrgx.logging import enable_logging, logger
from mvrgx.project import PROJECT_ROOT, VERSION
from mvrgx.util import glob_sep

STYLE_PATH: Path = PROJECT_ROOT / 'gui/asset/qstyle.css'

STYLE_VAR_DEF_RGX: re.Pattern = re.compile(r"(--.+?): (.+);")
STYLE_VAR_ACCESS_RGX: re.Pattern = re.compile(r"var\((.+)\)")

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

class DialogOK(QDialog):
    def __init__(self, style_sheet: str = ''):
        super().__init__()
        self.ui = Ui_DialogOK()
        self.ui.setupUi(self)
        self.style_sheet = style_sheet
        self.setStyleSheet(style_sheet)

class MainWindow(QMainWindow):
    def __init__(self, style_sheet: str = ''):
        logger.info('Initializing main UI...')
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.style_sheet = style_sheet
        self.setStyleSheet(style_sheet)
        self.setWindowTitle(f'mvrgx v{VERSION}')

        # Signals
        logger.info('Connecting signals...')
        self.ui.pushButtonSrcBrowse.clicked.connect(self._ask_src_dir)

        self.ui.lineEditSrcDir.setPlaceholderText(str(Path('.').resolve()))
        self.ui.lineEditSrcDir.editingFinished.connect(self._update_src_dir_preview)
        self.ui.lineEditSrcDir.textChanged.connect(self._verify_src_dir)
        self.ui.lineEditSrcDir.editingFinished.emit()

        self.ui.labelSrcDirErrMsg.setVisible(False)

        self.ui.listWidgetSrcContents.itemDoubleClicked.connect(self._append_to_src_dir)

        self.ui.lineEditInputRegex.editingFinished.connect(self._update_mv_preview)
        self.ui.lineEditInputRegex.editingFinished.emit()

        self.ui.lineEditOutputPattern.textChanged.connect(self._verify_output_pattern)
        self.ui.lineEditOutputPattern.editingFinished.connect(self._update_mv_preview)
        self.ui.lineEditOutputPattern.editingFinished.emit()

        self.ui.pushButtonRenameFiles.clicked.connect(self._rename_files_clicked)

        logger.info('UI init complete')

    @property
    def src_dir(self) -> Path:
        return Path(self.ui.lineEditSrcDir.text()).resolve()

    @property
    def input_regex(self) -> re.Pattern:
        return re.compile(self.ui.lineEditInputRegex.text())

    @property
    def output_pattern(self) -> str:
        return self.ui.lineEditOutputPattern.text()

    @property
    def recurs_search(self) -> bool:
        return self.ui.checkBoxRecursive.isChecked()

    def _verify_src_dir(self):
        self.ui.labelSrcDirErrMsg.setVisible(not Path(self.ui.lineEditSrcDir.text()).is_dir())

    def _verify_output_pattern(self):
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
            self.ui.lineEditOutputPattern.setStyleSheet("color: black;")
        else:
            self.ui.lineEditOutputPattern.setStyleSheet("color: red;")

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

        contents_dirs, contents_files = glob_sep(self.src_dir, '*', recurs=self.recurs_search, sort=True)

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
        self.ui.listWidgetMvBefore.clear()
        self.ui.listWidgetMvAfter.clear()

        if not self.src_dir.is_dir():
            return

        contents_dirs, contents_files = glob_sep(self.src_dir, '*', recurs=self.recurs_search)

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
            self.ui.listWidgetMvBefore.addItem(item)

        if self.output_pattern and (self.ui.labelOutputPatternWarning.toolTip() == ''):
            for m in matched_dirs + matched_files:
                item = QListWidgetItem()
                full_path: Path = self.src_dir / m.string
                try:
                    parsed: str = parse_output_pattern(self.output_pattern, m, full_path, warn_no_group=False)
                    item.setText(parsed + ('/' if full_path.is_dir() else ''))
                except (AttributeError, ValueError) as e:
                    dlg = DialogOK(self.style_sheet)
                    dlg.setWindowTitle('Error parsing output pattern')
                    dlg.ui.labelMessage.setText(f'{e.__class__.__name__}: {e}')
                    dlg.exec()
                    break
                self.ui.listWidgetMvAfter.addItem(item)

    def _rename_files_clicked(self):
        pass

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
