import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QComboBox, QPushButton,
                             QLabel, QVBoxLayout)

class startWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.count = 0
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('1. activated')
        self.combo = QComboBox()
        self.combo.addItems(['apple', 'banana', 'cherry'])
        #self.combo.activated.connect(self.on_activated)
        self.combo.currentIndexChanged.connect(self.on_index_changed)
        btn = QPushButton('Change by code')
        btn.clicked.connect(self.change_by_code)

        self.label = QLabel('Signal count: 0')

        layout = QVBoxLayout()
        layout.addWidget(self.combo)
        layout.addWidget(btn)
        layout.addWidget(self.label)
        self.setLayout(layout)
        self.show()

    def on_activated(self, idx):
        self.count += 1
        self.label.setText(f'Signal count: {self.count}\n'
                          f'index={idx}, text={self.combo.currentText()}')
    
    def on_index_changed(self, idx):
        self.count += 1
        self.label.setText(f'Signal count: {self.count}\n'
                          f'index={idx}, text={self.combo.currentText()}')

    def change_by_code(self):
        self.combo.setCurrentIndex(2)

    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = startWindow()
    sys.exit(app.exec())