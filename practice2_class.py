import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

def on_click():
    mes = le1.text()
    if not mes:
        return
    lb2.setText(mes)
    w2.show()

def on_click_clear():
    w2.hide()

app = QApplication(sys.argv)

w1 = QWidget()
w1.setFixedSize(400, 300)
w1.setWindowTitle("w1")
w1.setStyleSheet("background-color: Winter white")

lb1 = QLabel("당나귀", w1)
lb1.resize(400, 100)
lb1.setAlignment(Qt.AlignmentFlag.AlignCenter)
lb1.setStyleSheet("font-size: 18px; padding: 5px; font-weight: bold; border: 2px solid green; border-radius: 10px;")

le1 = QLineEdit(w1)
le1.resize(200, 30)
le1.move(100, 150)

le1.setStyleSheet("font-size: 14px; padding: 5px; border: 2px solid darkblue; border-radius: 10px;  color: darkblue")
le1.setPlaceholderText("다음 단어를 입력하세요")

b1 = QPushButton("확인", w1)
b1.setStyleSheet("background-color: lightgreen")
b1.resize(90, 30)
b1.move(100, 200)
b1.clicked.connect(on_click)

b2 = QPushButton("지우기", w1)
b2.setStyleSheet("background-color: red")
b2.resize(90, 30)
b2.move(210, 200)
b2.clicked.connect(on_click_clear)

w2 = QWidget()
w2.setWindowTitle("w2")
w2.setStyleSheet("background-color: white")

lb2 = QLabel(" ", w2)
lb2.resize(400, 100)
lb2.setAlignment(Qt.AlignmentFlag.AlignCenter)
lb2.setStyleSheet("font-size: 18px; padding: 5px; font-weight: bold; border: 2px solid green; border-radius: 10px;")

pixmap = QPixmap("GUI-Programming/assets/image.png")
im_lb = QLabel(w2)
im_lb.setPixmap(pixmap)
im_lb.setScaledContents(True)
im_lb.resize(200,200)
im_lb.move(100, 100)

w1.show()

sys.exit(app.exec_())