import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,  QLabel
from PyQt5.QtGui import QPixmap, QIcon, QFont
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setGeometry(700,250,800,500)
        self.setWindowTitle("Hello GUI")
        self.setWindowIcon(QIcon("C:/Users/sabhy/Desktop/python/gui/pic.jpg"))
        
        heading=QLabel("GUI ineterface",self)
        heading.setGeometry(0,0,800,100)
        heading.setFont(QFont("Algerian",30))
        heading.setStyleSheet("color: black;"
                            "background-color: #757b82;"
                            "text-decoration:underline;")
        heading.setAlignment(Qt.AlignCenter)

        
        label=QLabel("Hello Guys! My name is Sabhya Singh.\nAnd This is my Gui program.",self)
        label.setGeometry(0,100,800,200)
        label.setFont(QFont("Cascadia Mono",15))
        label.setStyleSheet("color: #aa20f5;"
                            "background-color: #06274f;")
        
        pic_text=QLabel("And Here is my picture-->",self) # I remove my pic and add my name picture 
        pic_text.setGeometry(0,300,375,100)
        pic_text.setFont(QFont("Cascadia Mono",15))

        pict=QLabel(self)
        pict.setGeometry(375,300,800-375,200)
        pixmap=QPixmap("pic.jpg")
        pict.setPixmap(pixmap)
        pict.setScaledContents(True)


def main():
    app=QApplication(sys.argv)
    window=MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__=="__main__":
    main()
        