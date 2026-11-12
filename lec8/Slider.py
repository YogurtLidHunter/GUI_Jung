import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QSlider, QPushButton,
                             QLabel, QVBoxLayout)

class startWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.count = 0
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('2. Slider')
        self.slider = QSlider()
        self.slider.setMinimum(0)
        self.slider.setMaximum(100)
        self.slider.setTickInterval(10)
        self.slider.setTickPosition(QSlider.TicksBelow)
        self.slider.setSingleStep(1)
        self.slider.setPageStep(10)
        
        self.slider.valueChanged.connect(self.on_value_changed)

        btn = QPushButton('Change by code')
        
        btn.clicked.connect(self.change_by_code)

        self.label = QLabel('Signal count: 0\nvalue=0')


        layout = QVBoxLayout()
        layout.addWidget(self.slider)
        layout.addWidget(btn)
        layout.addWidget(self.label)
        self.setLayout(layout)
        self.show()
    
    def on_value_changed(self, value):
        self.count += 1
        self.label.setText(f'Signal count: {self.count}\n'
                          f'value={value}')

    def change_by_code(self):
        self.slider.setValue(50)
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = startWindow()
    sys.exit(app.exec())