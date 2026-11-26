import sys
from PyQt5.QtGui import QKeySequence
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QAction, QPlainTextEdit
)

class startWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("3. QMenu")
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
        file_menu.addSeparator()
        file_menu.addAction(self.quit_action)

        view_menu = mbar.addMenu('&View')
        preview_menu = view_menu.addMenu('&Preview')
        preview_menu.addAction(self.clear_action)

    def show_sample(self):
        self.preview.setPlainText('Hi')
        self.statusBar().showMessage('sample', 2500)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = startWindow()
    window.show()
    sys.exit(app.exec())
