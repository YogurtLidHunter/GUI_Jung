import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

n = 0

def btn_click():
    global n
    n += 1
    img_path = f"GUI-Programming/assets/image{n%6+1}.png"
    image_label.setPixmap(QPixmap(img_path))

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("실습 2 - 사용자 정보 입력")
window.setFixedSize(450, 350)

img_path = "GUI-Programming/assets/image1.png"

image_label = QLabel(window)
image_label.setGeometry(100, 100, 250, 200) # 위치 (100, 100), 크기 250x200
pixmap = QPixmap(img_path)
image_label.setPixmap(pixmap)
image_label.setScaledContents(True)

btn = QPushButton("클릭", window)
btn.show()

btn.clicked.connect(btn_click)

window.show()
sys.exit(app.exec_())