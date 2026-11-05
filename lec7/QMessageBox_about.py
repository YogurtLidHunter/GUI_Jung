import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLineEdit,
                             QLabel, QVBoxLayout, QMessageBox)

class startWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('2. about')

        button1 = QPushButton('About')
        button1.clicked.connect(self.show_app_info)
        button2 = QPushButton('About Qt')
        button2.clicked.connect(self.show_qt_info)

        layout = QVBoxLayout()
        layout.addWidget(button1)
        layout.addWidget(button2)
        
        self.setLayout(layout)
        self.show()

    def show_app_info(self):
        QMessageBox.about(self, 'About', 'My App\nv1.0')

    def show_qt_info(self):
        QMessageBox.aboutQt(self, 'About Qt')

app = QApplication(sys.argv)
window = startWindow()
sys.exit(app.exec())