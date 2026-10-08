import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QHBoxLayout, QVBoxLayout,
)
from PyQt5.QtCore import Qt


class startWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("QHBoxLayout")
        self.setFixedSize(400, 200)
        self.setStyleSheet("background-color: #f0f0f0;")

        # Create horizontal box layout
        self.H_Layout = QHBoxLayout()
        self.V_Layout = QVBoxLayout()

        self.append_layout(self.H_Layout, "빨간색", 'red')
        self.append_layout(self.V_Layout, "주황색", 'orange')
        self.append_layout(self.V_Layout, "노란색", 'yellow')
        self.append_layout(self.V_Layout, "초록색", 'green')
        self.append_layout(self.V_Layout, "파랑색", 'blue')

        self.H_Layout.addLayout(self.V_Layout)
        self.setLayout(self.H_Layout)

    def append_layout(self, layout, text, color):
        label = QLabel(text, self)
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet(
            f"background-color: {color}; color: black; font-size: 24px;"
        )
        layout.addWidget(label)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = startWindow()
    window.show()
    sys.exit(app.exec_())
