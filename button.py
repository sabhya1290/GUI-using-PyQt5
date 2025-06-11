import sys
from PyQt5.QtWidgets import QApplication, QPushButton, QLabel,QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(600,250,500,500)
        self.button=QPushButton("click me",self)
        self.label=QLabel("Hello",self)
        self.initUI()

    def initUI(self):
        self.button.setGeometry(100,100,200,100)
        self.button.setStyleSheet("font-size : 30px;")
        self.button.clicked.connect(self.on_click)
        self.label.setGeometry(100,250,250,150)
        self.label.setStyleSheet("font-size: 50px;")


    def on_click(self):
        self.label.setText("Good Bye!")
        self.button.setDisabled(True)

def main():
    app= QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()