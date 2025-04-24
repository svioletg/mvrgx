import re
import sys
from pathlib import Path

from PySide6.QtWidgets import QApplication, QDialog, QFileDialog, QListWidgetItem, QMainWindow

from mvrgx.core import parse_output_pattern
from mvrgx.gui.ui_dialog_ok import Ui_DialogOK
from mvrgx.gui.ui_main import Ui_MainWindow
from mvrgx.logging import enable_logging, logger
from mvrgx.project import PROJECT_ROOT, VERSION

STYLE_PATH: Path = PROJECT_ROOT / 'gui/asset/qstyle.css'

STYLE_VAR_RGX = re.compile(r"(--.+): (.+);")

def parse_style_sheet(fp: str | Path) -> str:
    style_raw: str = STYLE_PATH.read_text('utf-8')

    if (m := re.search(r":root {(.*?)}", style_raw, flags=re.S)) is None:
        style_root_inner: str = ''
        style_sheet: str = style_raw
    else:
        style_root_inner: str = str(m.groups(0)[0])
        style_sheet: str = style_raw[m.end(0):]

    for k, v in STYLE_VAR_RGX.findall(style_root_inner):
        style_sheet = style_sheet.replace(f'var({k})', v)
    return style_sheet

STYLE_SHEET: str = parse_style_sheet(STYLE_PATH)

class DialogOK(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_DialogOK()
        self.ui.setupUi(self)
        self.setStyleSheet(STYLE_SHEET)

class MainWindow(QMainWindow):
    def __init__(self):
        logger.info('Initializing main UI...')
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setStyleSheet(STYLE_SHEET)
        self.setWindowTitle(f'mvrgx v{VERSION}')

        # Signals
        logger.info('Connecting signals...')
        self.ui.pushButtonSrcBrowse.clicked.connect(self._ask_src_dir)

        self.ui.lineEditSrcDir.setPlaceholderText(str(Path('.').resolve()))
        self.ui.lineEditSrcDir.editingFinished.connect(self._update_src_dir_preview)
        self.ui.lineEditSrcDir.textChanged.connect(self._verify_src_dir)
        self.ui.lineEditSrcDir.editingFinished.emit()

        self.ui.labelSrcDirMissing.setVisible(False)

        self.ui.listWidgetSrcContents.itemDoubleClicked.connect(self._append_to_src_dir)

        self.ui.lineEditInputRegex.editingFinished.connect(self._update_mv_preview)
        self.ui.lineEditOutputPattern.textChanged.connect(self._verify_output_pattern)
        self.ui.lineEditOutputPattern.editingFinished.connect(self._update_mv_preview)

        logger.info('UI init complete')

    @property
    def src_dir(self) -> Path:
        return Path(self.ui.lineEditSrcDir.text()).resolve()

    @property
    def find_regex(self) -> re.Pattern:
        return re.compile(self.ui.lineEditInputRegex.text())

    @property
    def output_pattern(self) -> str:
        return self.ui.lineEditOutputPattern.text()

    @property
    def recurs_search(self) -> bool:
        return self.ui.checkBoxRecursive.isChecked()

    def _verify_src_dir(self):
        self.ui.labelSrcDirMissing.setVisible(not Path(self.ui.lineEditSrcDir.text()).is_dir())

    def _verify_output_pattern(self):
        self.ui.labelOutputPatternMissing.setVisible(not self.output_pattern)

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

        contents_dirs: list[Path] = []
        contents_files: list[Path] = []
        for f in self.src_dir.glob('*'):
            (contents_dirs if f.is_dir() else contents_files).append(f)

        contents_dirs.sort()
        contents_files.sort()

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

        full_glob: list[Path] = list((self.src_dir.rglob('*') if self.recurs_search else self.src_dir.glob('*')))
        matched: list[re.Match[str]] = [
            m for f in full_glob \
            if (m := self.find_regex.search(str(f.relative_to(self.src_dir))))
        ]

        matched.sort(key=lambda i: i.string)

        for m in matched:
            item = QListWidgetItem()
            item.setText(m.string)
            self.ui.listWidgetMvBefore.addItem(item)

        if self.output_pattern:
            for m in matched:
                item = QListWidgetItem()
                try:
                    item.setText(parse_output_pattern(self.output_pattern, m, self.src_dir / m.string))
                except (AttributeError, IndexError, ValueError) as e:
                    dlg = DialogOK()
                    dlg.setWindowTitle('Error parsing output pattern')
                    dlg.ui.labelMessage.setText(f'{e.__class__.__name__}: {e}')
                    dlg.exec()
                    break
                self.ui.listWidgetMvAfter.addItem(item)

def run_gui() -> int | None:
    enable_logging(logger, 'INFO')

    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    logger.info('Executing...')
    return app.exec()

if __name__ == '__main__':
    sys.exit(run_gui())
