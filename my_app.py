from second_win import *


class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.next_click()
        self.show()

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

    def initUI(self):
        self.hello_text = QLabel(txt_hello)
        self.insctruction = QLabel(txt_instruction)
        self.bnt_next = QPushButton(txt_next)
        self.layoutV = QVBoxLayout()
        self.layoutV.addWidget(self.hello_text, alignment=Qt.AlignLeft)
        self.layoutV.addWidget(self.insctruction, alignment=Qt.AlignLeft)
        self.layoutV.addWidget(self.bnt_next, alignment=Qt.AlignCenter)
        self.setLayout(self.layoutV)

    def connects(self):
        self.bnt_next.clicked.connect(self.next_click)

    def next_click(self):
        self.hide()
        self.tw = TestWin()



app = QApplication([])
window = MainWin()
app.exec_()
    
