import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLineEdit,
                             QLabel, QVBoxLayout, QMessageBox)

class startWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.data = []
        self.setWindowTitle('3. question')

        button = QPushButton('Ask')
        button.clicked.connect(self.ask)
        self.label = QLabel(f'data: {self.data}')

        layout = QVBoxLayout()
        layout.addWidget(button)
        
        self.setLayout(layout)
        self.show()

    def ask(self):
        QMessageBox.question(self, 'Ask', 'select 1', QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
                             | QMessageBox.StandardButton.Cancel)

app = QApplication(sys.argv)
window = startWindow()
sys.exit(app.exec())