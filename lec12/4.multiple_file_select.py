import sys
from pathlib import Path
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel,
                             QListWidget, QVBoxLayout, QFileDialog)


class startWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("4. Select multiple files")
        self.resize(640, 320)
        button = QPushButton("Select files (Ctrl / Cmd / Shift)")
        button.clicked.connect(self.select_files)
        self.label = QLabel("Selected: 0 files")
        self.file_list = QListWidget()

        layout = QVBoxLayout()
        layout.addWidget(button)
        layout.addWidget(self.label)
        layout.addWidget(self.file_list)
        self.setLayout(layout)
        self.show()

    def select_files(self):
        # getOpenFileNames: 첫 번째 반환값이 str 대신 list[str]
        file_names, selected_filter = QFileDialog.getOpenFileNames(
            self, "Select multiple files", str(Path(__file__).resolve().parent / "samples"),
            "Text files (*.txt *.md);;All files (*)")

        # Cancel -> 빈 리스트 [] / 이전 목록은 그대로 유지
        if not file_names:
            self.label.setText(f"Selection cancelled. Kept {self.file_list.count()} files.")
            return

        self.file_list.clear()
        self.file_list.addItems(file_names)
        self.label.setText(f"Selected: {len(file_names)} files")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = startWindow()
    sys.exit(app.exec())
