import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout
from PyQt5.QtCore import Qt, QTimer, QTime
from PyQt5.QtGui import QFont, QFontDatabase

class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()
        self.time_label=QLabel(self)
        self.timer=QTimer(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Digital Clock")
        self.setGeometry(800, 400, 350, 100)

        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        self.setLayout(vbox)
        self.time_label.setAlignment(Qt.AlignCenter)

        self.time_label.setStyleSheet("font-size:100px;"
                                      "color:hsl(99, 98%, 50%);"
                                      )
        
        font_id= QFontDatabase.addApplicationFont("gui/DS-DIGIB.TTF")
        font_family=QFontDatabase.applicationFontFamilies(font_id)[0]
        my_font=QFont(font_family,100)
        self.time_label.setFont(my_font)
        
        self.setStyleSheet("background-color:black;")
        
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)
        
        self.update_time()


    def update_time(self):
        current_time= QTime.currentTime().toString("hh:mm:ss AP")
        self.time_label.setText(current_time)

def main():
    app=QApplication(sys.argv)
    clock=DigitalClock()
    clock.show()
    sys.exit(app.exec_())

if __name__=="__main__":
    main()