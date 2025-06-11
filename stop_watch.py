import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QPushButton, QGridLayout, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt, QTimer, QTime
from PyQt5.QtGui import QFont, QFontDatabase

class StopWatch(QWidget):
    def __init__(self):
        super().__init__()

        self.time = QTime(0, 0, 0, 0)
        self.time_label=QLabel("00:00:00.00",self)
        self.timer=QTimer(self)

        self.start_button=QPushButton("Start",self)
        self.stop_button=QPushButton("Stop",self)
        self.reset_button=QPushButton("Reset",self)

        self.initUI()

    def initUI(self):



        self.setWindowTitle("Stop Watch")
        self.setGeometry(800, 400, 350, 200)

        vbox=QVBoxLayout()
        vbox.addWidget(self.time_label)

        self.setLayout(vbox)
        self.time_label.setAlignment(Qt.AlignCenter)

        hbox=QHBoxLayout()
        hbox.addWidget(self.start_button)
        hbox.addWidget(self.stop_button)
        hbox.addWidget(self.reset_button)
        vbox.addLayout(hbox)

        self.setStyleSheet("""
                           QPushButton,QLabel
                           {
                                padding:20px;
                                border: 1px solid black;
                                font-weight:bold;
                           }

                           QPushButton
                           {
                                font-size : 40px;
                                font-family: Arial;
                           }
                           """)



        # grid=QGridLayout()
        # grid.addWidget(self.time_label,0,0,1,6)
        # grid.addWidget(self.start_button,1,0,1,2)
        # grid.addWidget(self.stop_button,1,2,1,2)
        # grid.addWidget(self.reset_button,1,4,1,2)
        # self.setLayout(grid)

        self.time_label.setStyleSheet("font-size:100px;"
                                      "color:black;"
                                      "background-color:cyan;"
                                      "border-radius:20px;"
                                      )
        
        font_id= QFontDatabase.addApplicationFont("gui/DS-DIGIB.TTF")
        font_family=QFontDatabase.applicationFontFamilies(font_id)[0]
        my_font=QFont(font_family,100)
        self.time_label.setFont(my_font)
        
        self.start_button.clicked.connect(self.start)
        self.stop_button.clicked.connect(self.stop)
        self.reset_button.clicked.connect(self.reset)

        self.timer.timeout.connect(self.update_display)
        # self.timer.start(1000)
        # self.update_time()
    
    def start(self):
        self.timer.start(10)

    def stop(self):
        self.timer.stop()

    def reset(self):
        self.timer.stop()
        self.time=QTime(0 , 0 , 0 , 0)
        self.time_label.setText(self.format_time(self.time))

    def format_time(self, time):
        hours=time.hour()
        minutes=time.minute()
        seconds=time.second()
        millisecond=time.msec()//10
        return f"{hours:02}:{minutes:02}:{seconds:02}.{millisecond:02}"

    def update_display(self):
        self.time=self.time.addMSecs(10)
        self.time_label.setText(self.format_time(self.time)) 

def main():
    app=QApplication(sys.argv)
    clock=StopWatch()
    clock.show()
    sys.exit(app.exec_())

if __name__=="__main__":
    main()