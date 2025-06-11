import sys
from PyQt5.QtWidgets import QLabel, QApplication, QMainWindow
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(100,100,800,800)

        label=QLabel("Hello",self)
        label.setFont(QFont("Ariel",30))
        label.setGeometry(0,0,800,100)
        label.setStyleSheet("color:#3ed6d6;"
                            "background-color: #4643a3;"
                            "font-weight: bold;"
                            "font-style: Italic;"
                            "text-decoration:underline;")
        # label.setAlignment(Qt.AlignTop) #Vertically top
        # label.setAlignment(Qt.AlignBottom) #Vertically bottom
        # label.setAlignment(Qt.AlignVCenter) #Vertically centre
        # label.setAlignment(Qt.AlignRight) #Horizontally right
        # label.setAlignment(Qt.AlignLeft) #Horizontally left
        # label.setAlignment(Qt.AlignHCenter) #Horizontally centre
        # label.setAlignment(Qt.AlignHCenter | Qt.AlignBottom) #Horizontally centre and vertically bottom
        # label.setAlignment(Qt.AlignHCenter | Qt.AlignTop) #Horizontally centre and vertically top
        
        label.setAlignment(Qt.AlignCenter) #h and v both centre

        

def main():
    app = QApplication(sys.argv)
    window=MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()