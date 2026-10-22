import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout)
from PyQt5.QtCore import QObject, pyqtSignal

class Counter(QObject):
    changed = pyqtSignal(int)

    def __init__(self):
        super().__init__()
        self.value = 0

    def add_one(self):
        self.value += 1
        self.changed.emit(self.value)

class startWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.counter = Counter()
        self.init_ui()
        self.counter.changed.connect(self.show_value)

    def init_ui(self):
        self.setWindowTitle("7. Signal with Meaning")
        button = QPushButton("+1")
        button.clicked.connect(self.counter.add_one)
        self.label = QLabel("0")
        layout = QVBoxLayout()
        layout.addWidget(button)
        layout.addWidget(self.label)
        self.setLayout(layout)
        self.show()

    def show_value(self, value):
        self.label.setText(str(value))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = startWindow()
    sys.exit(app.exec_())