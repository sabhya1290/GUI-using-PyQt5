import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QPixmap, QFont


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(600,200,700,600)
        
        label1=QLabel("Hello, this is me.",self)
        label1.setFont(QFont("Roboto Slab",20))
        label1.setGeometry(0,0,700,100)

        label=QLabel(self)
        label.setGeometry(0,0,300,200)

        pixmap= QPixmap("pic.jpg")
        label.setPixmap(pixmap)

        label.setScaledContents(True)
        label.setGeometry((self.width()-label.width())//2,(self.height()-label.height())//2,label.width(),label.height())

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()