import sys
from PyQt5.QtGui import QKeySequence
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QAction, QPlainTextEdit, QFileDialog, QMessageBox
)
from pathlib import Path

class startWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("3. QMenu upgrade")
        self.resize(620, 360)
        self.preview = QPlainTextEdit()
        self.preview.setReadOnly(True)
        self.setCentralWidget(self.preview)
        self.statusBar().showMessage('Ready')
        self.create_actions()
        self.create_menu()

    def create_actions(self):
        self.sample_action = QAction("Show &sample", self)
        self.sample_action.setShortcut("Ctrl+L")
        self.sample_action.setStatusTip('Ay')
        self.sample_action.triggered.connect(self.show_sample)

        self.file_open_action = QAction('&오쁜파일', self)
        self.file_open_action.setShortcut(QKeySequence.Open)
        self.file_open_action.setStatusTip('오픈더텍스트파일')
        self.file_open_action.triggered.connect(self.open_file)

        self.clear_action = QAction('&Clear', self)
        self.clear_action.triggered.connect(self.preview.clear)

        self.quit_action = QAction('&Quit', self)
        self.quit_action.setShortcut(QKeySequence.Quit)
        self.quit_action.triggered.connect(self.close)

    def create_menu(self):
        mbar = self.menuBar()
        mbar.setNativeMenuBar(False)
        file_menu = mbar.addMenu('&File')
        file_menu.addAction(self.sample_action)
        file_menu.addAction(self.file_open_action)
        file_menu.addSeparator()
        file_menu.addAction(self.quit_action)

        view_menu = mbar.addMenu('&View')
        preview_menu = view_menu.addMenu('&Preview')
        preview_menu.addAction(self.clear_action)

    def show_sample(self):
        self.preview.setPlainText('Hi')
        self.statusBar().showMessage('sample', 2500)

    def open_file(self):
        data = self.open_file_dialog()
        if data is not None:
            self.preview.setPlainText(data)
            self.statusBar().showMessage('File loaded', 2500)

    def open_file_dialog(self):
        fm, sf = QFileDialog.getOpenFileName(
            self, 'Open', str(Path(__file__).resolve().parent / 'samples'),
            'Text files (*.txt *.md *.py);;Apple File (*.Apple);;All files (*)')
        if not fm:
            return

        try:
            with open(fm, 'r') as file:
                data = file.read()
            return data
        except (OSError, UnicodeError) as error:
            QMessageBox.warning(self, 'a', 'aads')
            return

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = startWindow()
    window.show()
    sys.exit(app.exec())
