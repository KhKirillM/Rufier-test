from final_win import *

class Experiment():
    def __init__(self, age, test1, test2, test3):
        self.age = int(age)
        self.t1 = int(test1)
        self.t2 = int(test2)
        self.t3 = int(test3)


class TestWin(QWidget):

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
        self.h_line = QHBoxLayout()
        self.r_line = QVBoxLayout()
        self.l_line = QVBoxLayout()
        self.name_txt = QLabel(txt_name)
        self.age_txt = QLabel(txt_age)
        self.test1_txt = QLabel(txt_test1)
        self.test2_txt = QLabel(txt_test2)
        self.test3_txt = QLabel(txt_test3)
        self.text_timer = QLabel()
        self.starttest1_txt = QPushButton(txt_starttest1)
        self.starttest2_txt = QPushButton(txt_starttest2)
        self.starttest3_txt = QPushButton(txt_starttest3)
        self.bnt_next = QPushButton(txt_sendresults)
        self.hintname_txt = QLineEdit(txt_hintname)
        self.hintage_txt = QLineEdit(txt_hintage)
        self.hinttest1_txt = QLineEdit(txt_hinttest1)
        self.hinttest2_txt = QLineEdit(txt_hinttest2)
        self.hinttest3_txt = QLineEdit(txt_hinttest3)
        self.l_line.addWidget(self.name_txt, alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.hintname_txt, alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.age_txt, alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.hintage_txt, alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.test1_txt, alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.starttest1_txt, alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.hinttest1_txt, alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.test2_txt, alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.starttest2_txt, alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.test3_txt, alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.starttest3_txt, alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.hinttest2_txt, alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.hinttest3_txt, alignment=Qt.AlignLeft)
        self.r_line.addWidget(self.text_timer, alignment=Qt.AlignRight)
        self.l_line.addWidget(self.bnt_next, alignment=Qt.AlignCenter)
        self.h_line.addLayout(self.l_line)
        self.h_line.addLayout(self.r_line)
        self.setLayout(self.h_line)

    def timer_test(self):
        global time
        time = QTime(0, 0, 15)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer1Event)
        self.timer.start(1000)

    def timer_sits(self):
        global time
        time = QTime(0, 0, 30)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer2Event)
        self.timer.start(1500)

    def timer_final(self):
        global time
        time = QTime(0, 1, 0)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer3Event)
        self.timer.start(1000)

    def timer1Event(self):
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString('hh:mm:ss'))
        self.text_timer.setFont(QFont('Times', 36, QFont.Bold))
        self.text_timer.setStyleSheet('color: rgb(0, 0, 0)')
        if time.toString('hh:mm:ss') == '00:00:00':
            self.timer.stop()

    def timer2Event(self):
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString('hh:mm:ss')[6:8])
        self.text_timer.setFont(QFont('Times', 36, QFont.Bold))
        self.text_timer.setStyleSheet('color: rgb(0, 0, 0)')
        if time.toString('hh:mm:ss') == '00:00:00':
            self.timer.stop()

    def timer3Event(self): 
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString('hh:mm:ss'))
        if int(time.toString('hh:mm:ss')[6:8]) >= 45:
            self.text_timer.setStyleSheet('color: rgb(0, 255, 0)')
        elif int(time.toString('hh:mm:ss')[6:8]) <= 15:
            self.text_timer.setStyleSheet('color: rgb(0, 255, 0)')
        else:
            self.text_timer.setStyleSheet('color: rgb(0, 0, 0)')
        if time.toString('hh:mm:ss') == '00:00:00':
            self.timer.stop()
        
    def connects(self):
        self.bnt_next.clicked.connect(self.next_click)
        self.starttest1_txt.clicked.connect(self.timer_test)
        self.starttest2_txt.clicked.connect(self.timer_sits)
        self.starttest3_txt.clicked.connect(self.timer_final)

    def next_click(self):
        self.hide()
        self.exp = Experiment(self.hintage_txt.text(), self.hinttest1_txt.text(), self.hinttest2_txt.text(), self.hinttest3_txt.text())
        self.fw = FinalWin(self.exp)

