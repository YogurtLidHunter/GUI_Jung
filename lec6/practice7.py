import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout)
from PyQt5.QtCore import pyqtSignal

class startWindow(QWidget):
    # "clicked" 보다 의미 있는 signal 을 직접 만등
    login_ok = pyqtSignal(str)
    login_failed = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.init_ui()
        self.login_ok.connect(self.welcome)
        self.login_failed.connect(self.show_error)

        self.users = {
            "q" : "1",
            "w" : "2",
            "e" : "3",
        }

    def init_ui(self):
        self.setWindowTitle("7. Signal with Meaning")
        self.username = QLineEdit()
        self.username.setPlaceholderText("Username")

        
        self.edit = QLineEdit()
        self.edit.setPlaceholderText("Password")
        self.edit.setEchoMode(QLineEdit.EchoMode.Password)
        button = QPushButton("Login")
        button.clicked.connect(self.check_password) # 45 signal
        self.label = QLabel("")

        layout = QVBoxLayout()
        layout.addWidget(self.username)
        layout.addWidget(self.edit)
        layout.addWidget(button)
        layout.addWidget(self.label)
        self.setLayout(layout)
        self.show()

    def check_password(self):
        user = self.username.text()
        password = self.edit.text()

        if user not in self.users:
            self.login_failed.emit(f"Unknown user: {user}")
        elif self.users[user] != password:
            self.login_failed.emit("Wrong password")
        else:
            self.login_ok.emit(user)

    # slot
    def welcome(self, name):
        self.label.setText(f"Welcome, {name}!")

    def show_error(self, text):
        self.label.setText(text)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = startWindow()
    sys.exit(app.exec_())