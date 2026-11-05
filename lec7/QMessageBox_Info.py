import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLineEdit,
                             QLabel, QVBoxLayout, QMessageBox)

class startWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('1. info')

        self.user_name = QLineEdit()
        
        self.user_age = QLineEdit()

        button = QPushButton('sumbit')
        button.clicked.connect(self.show_info)
        self.label = QLabel('')

        layout = QVBoxLayout()
        layout.addWidget(self.user_name)
        layout.addWidget(self.user_age)
        layout.addWidget(button)
        
        self.setLayout(layout)
        self.show()

    def show_info(self):
        name = self.user_name.text()
        age = self.user_age.text()
        QMessageBox.information(self, 'info', f'{name}\n{age}')

app = QApplication(sys.argv)
window = startWindow()
sys.exit(app.exec())