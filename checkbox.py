import sys
from PyQt5.QtWidgets import QApplication, QCheckBox, QLabel,QMainWindow
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(600,250,500,500)
        self.checkbox=QCheckBox("Do you like food?",self)

        self.initUI()

    def initUI(self):
        self.checkbox.setGeometry(10,0,300,100)
        self.checkbox.setStyleSheet("font-size:30px;"
                                    "font-family: Arial;")
        # self.checkbox.setChecked(True)
        self.checkbox.stateChanged.connect(self.checkbox_changed)

    def checkbox_changed(self,state):
        if state == Qt.Checked:
            print("You like food ")        

def main():
    app= QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()