import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QGridLayout,
)
from PyQt5.QtCore import Qt


class startWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("QGridLayout")
        self.setFixedSize(400, 200)
        self.setStyleSheet("background-color: #f0f0f0;")

        layout = QGridLayout()

        label1 = self.make_label('이름', 'blue')
        layout.addWidget(label1, 0, 0)

        label2 = self.make_label('', 'white')
        layout.addWidget(label2, 1, 0, 2, 1)

        label2 = self.make_label('', 'white')
        layout.addWidget(label2, 1, 1, 2, 1)

        label2 = self.make_label('', 'white')
        layout.addWidget(label2, 3, 0, 2, 1)

        label2 = self.make_label('', 'white')
        layout.addWidget(label2, 3, 1, 2, 1)

        label3 = self.make_label('이름을 입력하세요', 'white')
        layout.addWidget(label3, 0, 1, 1, 2)

        label4 = self.make_label('이름', 'pink')
        layout.addWidget(label4, 1, 2, 4, 1)

        self.setLayout(layout)

    def make_label(self, text, color):
        label = QLabel(text, self)
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet(
            f"background-color: {color}; color: black; font-size: 24px;"
        )
        return label
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = startWindow()
    window.show()
    sys.exit(app.exec_())
