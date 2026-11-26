import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QAction, QPushButton
)

class startWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.count = 0
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("2. QAction and shortcuts")
        self.resize(560, 280)
        self.button = QPushButton("Count: 0")
        self.setCentralWidget(self.button)

        self.count_action = QAction("Count", self)
        self.count_action.setShortcut("Ctrl+L")
        self.count_action.triggered.connect(self.add_one)
        # 메뉴나 툴바를 사용하기 전에는 창에 직접 등록
        self.addAction(self.count_action)
        self.button.clicked.connect(self.count_action.trigger)
        self.statusBar().showMessage("Click the button or press Ctrl+L (Command+L on Mac).")

    def add_one(self):
        self.count += 1
        self.button.setText(f"Count: {self.count}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = startWindow()
    window.show()
    sys.exit(app.exec())
