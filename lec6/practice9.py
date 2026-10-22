import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout)
from PyQt5.QtCore import pyqtSignal

class ColorPicker(QWidget):
    color_chosen = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        layout = QHBoxLayout()
        for color in ["red", "green", "blue"]:
            button = QPushButton(color)
            button.clicked.connect(self.on_click)
        self.setLayout(layout)

    def on_click(self):
        self.color_chosen.emit(self.sender().text())

class startWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("9. Signal with Meaning")
        self.label = QLabel("Pick")
        picker = ColorPicker()
        picker.color_chosen.connect(self.set_color)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(picker)
        self.setLayout(layout)
        self.show()

    def set_color(self, color):
        self.label.setText(color)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = startWindow()
    sys.exit(app.exec_())