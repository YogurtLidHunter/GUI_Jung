import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QSpinBox, QPushButton,
                             QLabel, QVBoxLayout)

class startWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.count = 0
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('1. QSpinBox')
        self.spin = QSpinBox()

        self.spin.setMinimum(0)
        self.spin.setMaximum(100)
        self.spin.setSingleStep(5)
        self.spin.setPrefix('$ ')
        self.spin.setSuffix(' USD')
        self.spin.setValue(20)

        set_btn = QPushButton('Set ')
        set_btn.clicked.connect(self.cbc)

        gb = QPushButton('Read ')
        gb.clicked.connect(self.rv)

        self.lb = QLabel('Press R')

        la = QVBoxLayout()
        la.addWidget(self.spin)
        la.addWidget(set_btn)
        la.addWidget(gb)
        la.addWidget(self.lb)
        self.setLayout(la)
        self.show()

    def cbc(self):
        self.spin.setValue(150)

    def rv(self):
        v = self.spin.value()
        self.lb.setText(f'{v}, ')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = startWindow()
    sys.exit(app.exec())
