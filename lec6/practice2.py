import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import pyqtSignal

class startWindow(QWidget):
    w_clicked = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.count = 0
        self.init_ui()
        self.w_clicked.connect(self.add_one)

    def init_ui(self):
        self.setWindowTitle("Hi")
        self.label = QLabel("Clicked : 0")
        self.btn = QLabel()
        self.btn.setGeometry(50, 50, 50, 50)
        self.btn.setStyleSheet(
            f"background-color: red; color: black;"
        )
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.btn)
        self.setLayout(layout)
        self.show()

    def mousePressEvent(self, event):
        if self.btn.geometry().contains(event.pos()):
            self.w_clicked.emit()

    def add_one(self):
        self.count += 1
        self.label.setText(f"Clicked : {self.count}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = startWindow()
    sys.exit(app.exec())
