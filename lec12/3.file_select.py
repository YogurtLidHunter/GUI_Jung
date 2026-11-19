import sys
from pathlib import Path
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel,
                             QVBoxLayout, QFileDialog)


class startWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("3. Select one file")
        self.resize(580, 220)
        button = QPushButton("Select a file")
        button.clicked.connect(self.select_file)
        self.label = QLabel("No file selected.")
        self.label.setTextFormat(Qt.PlainText)
        self.label.setWordWrap(True)

        layout = QVBoxLayout()
        layout.addWidget(button)
        layout.addWidget(self.label)
        self.setLayout(layout)
        self.show()

    def select_file(self):
        # 반환값은 (파일 경로 str, 선택한 필터 str) 튜플
        # 필터 그룹은 ;; 로 구분 / 한 그룹의 확장자는 공백으로 구분
        file_name, selected_filter = QFileDialog.getOpenFileName(
            self, "Select one file", str(Path(__file__).resolve().parent / "samples"),
            "Images (*.jpg *.jpeg);;")

        # Cancel을 누르면 file_name은 빈 문자열 ''
        if not file_name:
            self.label.setText("Selection cancelled.")
            return

        path = Path(file_name)
        self.label.setText(f"Name: {path.name}\n"
                           f"Path: {file_name}\nFilter: {selected_filter}")
        # 경로를 선택한 것뿐! 아직 파일 내용을 읽지는 않음


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = startWindow()
    sys.exit(app.exec())
