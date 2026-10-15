import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel)
from PyQt5.QtCore import Qt, QTime

class startWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

        self.start_time = None
        self.is_dark = False
        self.font_size = 12
        self.ctrl = False

    def init_ui(self):
        self.setGeometry(100, 100, 300, 200)
        self.setWindowTitle("Mouse Press Example")
        self.label = QLabel("<p>Click anywhere with any mouse button.</p>")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents)
        self.setCentralWidget(self.label)
        self.show()

    def mousePressEvent(self, event):
        if self.start_time is None:
            self.start_time = QTime.currentTime()

        # 어떤 버튼이 눌렸는지 확인
        if event.button() == Qt.MouseButton.LeftButton:
            button = "Left"
        elif event.button() == Qt.MouseButton.RightButton:
            button = "Right"
        elif event.button() == Qt.MouseButton.MiddleButton:
            button = "Middle"
        else:
            button = "Other"
        x, y = event.pos().x(), event.pos().y()
        print(f"{button} button pressed at ({x}, {y})")
        self.label.setText(f"<p><b>{button}</b> button pressed at ({x}, {y})</p>")

    def mouseReleaseEvent(self, event):
        if self.start_time is not None:
            current_time = QTime.currentTime()
            elapsed_time = self.start_time.msecsTo(current_time)
            self.label.setText(f"{elapsed_time / 1000:.2f} seconds")
            self.start_time = None

    def mouseMoveEvent(self, event):
        x, y = event.pos().x(), event.pos().y()
        self.label.setText(f"<p>Mouse position: ({x}, {y})</p>")

    def mouseDoubleClickEvent(self, event):
        self.is_dark = not self.is_dark
        if self.is_dark:
            self.setStyleSheet("background-color: black; color: white;")
        else:
            self.setStyleSheet("")

    def wheelEvent(self, event):
        if not self.ctrl:
            return
        
        if event.angleDelta().y() > 0:
            self.font_size = max(self.font_size - 1, 6)
        else:
            self.font_size = min(self.font_size + 1 , 60)
        self.update_font()

    def update_font(self):
        font = self.label.font()
        font.setPointSize(self.font_size)
        self.label.setFont(font)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Control:
            self.ctrl = True
            print("ctrl True")
    
    def keyReleaseEvent(self, event):
        if event.key() == Qt.Key.Key_Control:
            self.ctrl = False
            print("ctrl False")

    def enterEvent(self, event):
        self.label.setStyleSheet("background-color: lightgreen;")

    def leaveEvent(self, event):
        self.label.setStyleSheet("background-color: lightpink;")

    def resizeEvent(self, event):
        size = event.size()
        print(f"{size.width()} x {size.height()}")

    def moveEvent(self, event):
        pos = event.pos()
        print(f"{pos.x()}, {pos.y()}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = startWindow()
    sys.exit(app.exec())
