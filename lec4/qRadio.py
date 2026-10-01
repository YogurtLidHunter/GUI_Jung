import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QTextEdit, QLineEdit,
    QPushButton, QMessageBox, QRadioButton, QButtonGroup
)

class startWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("QTextEdit and QLineEdit")
        self.setFixedSize(500, 260)

        # label
        self.text_label = QLabel("성별", self)
        self.text_label.setGeometry(20, 20, 100, 30)

        # radio buttons
        self.male_radio = QRadioButton("남성", self)
        self.male_radio.setGeometry(20, 60, 100, 30)

        self.female_radio = QRadioButton("여성", self)
        self.female_radio.setGeometry(20, 100, 100, 30)

        self.nonbinary_radio = QRadioButton("논바이너리", self)
        self.nonbinary_radio.setGeometry(20, 140, 100, 30)

        self.sex_group = QButtonGroup(self)
        self.sex_group.addButton(self.male_radio)
        self.sex_group.addButton(self.female_radio)
        self.sex_group.addButton(self.nonbinary_radio)

        # Button
        self.button = QPushButton("제출", self)
        self.button.setGeometry(20, 180, 100, 30)
        self.button.clicked.connect(self.on_click)

        # result display label
        self.result_label = QLabel("Result", self)
        self.result_label.setGeometry(20, 200, 460, 100)
        self.result_label.hide()

    def on_click(self):
        selected = self.sex_group.checkedButton()
        if selected:
            self.result_label.setText(f'당신의 성별은 {selected.text()}군요.')
        else:
            self.result_label.setText('성별을 선택해주세요.')
        self.result_label.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = startWindow()
    window.show()
    sys.exit(app.exec_())
