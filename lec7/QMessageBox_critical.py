import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLineEdit,
                             QLabel, QVBoxLayout, QMessageBox)

class startWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.data = []
        self.setWindowTitle('4. critical')

        self.user_input = QLineEdit()
        button = QPushButton('Calculate 100 / number')
        button.clicked.connect(self.divide)
        self.label = QLabel('')

        layout = QVBoxLayout()
        layout.addWidget(self.user_input)
        layout.addWidget(button)
        
        self.setLayout(layout)
        self.show()

    def divide(self):
        try:
            number = float(self.user_input.text())
            self.label.setText(f'100 / {number} = {100/number}')
        except ValueError:
            QMessageBox.critical(self, 'Error')
        else:
            pass

app = QApplication(sys.argv)
window = startWindow()
sys.exit(app.exec())