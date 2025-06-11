import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QRadioButton, QButtonGroup

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(500, 200, 800, 600)
        self.radio1=QRadioButton("Visa",self)
        self.radio2=QRadioButton("Master Card",self)
        self.radio3=QRadioButton("American Express",self)
        self.radio4=QRadioButton("Online",self)
        self.radio5=QRadioButton("In Store",self)
        self.buttom_group1=QButtonGroup(self)
        self.buttom_group2=QButtonGroup(self)
        self.initUI()

    def initUI(self):
        self.radio1.setGeometry(0,0,400,100)
        self.radio2.setGeometry(0,50,400,100)
        self.radio3.setGeometry(0,100,400,100)
        self.radio4.setGeometry(0,150,400,100)
        self.radio5.setGeometry(0,200,400,100)
        
        self.setStyleSheet("QRadioButton{"
                           "font-size:40px;"
                           "font-family:Arial;"
                           "padding:10px;"
                           "}")
        
        self.buttom_group1.addButton(self.radio1)
        self.buttom_group1.addButton(self.radio2)
        self.buttom_group1.addButton(self.radio3)
        self.buttom_group2.addButton(self.radio4)
        self.buttom_group2.addButton(self.radio5)

        self.radio1.toggled.connect(self.radio_button_changed)
        self.radio2.toggled.connect(self.radio_button_changed)
        self.radio3.toggled.connect(self.radio_button_changed)
        self.radio4.toggled.connect(self.radio_button_changed)
        self.radio5.toggled.connect(self.radio_button_changed)

    def radio_button_changed(self):  
        radio_button= self.sender()
        if radio_button.isChecked():
            print(f"{radio_button.text()} is selected")



def main():
    app=QApplication(sys.argv)
    window=Window()
    window.show()
    sys.exit(app.exec_())

if __name__=="__main__":
    main()