import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QGridLayout, QHBoxLayout
from PyQt5.QtCore import Qt

class calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.r=""
        self.initUI()

    def initUI(self):

        l=QVBoxLayout()


        self._1=QPushButton("1",self)
        self._2=QPushButton("2",self)
        self._3=QPushButton("3",self)
        self._4=QPushButton("4",self)
        self._5=QPushButton("5",self)
        self._6=QPushButton("6",self)
        self._7=QPushButton("7",self)
        self._8=QPushButton("8",self)
        self._9=QPushButton("9",self)
        self._0=QPushButton("0",self)
        self._add=QPushButton("+",self) 
        self._sub=QPushButton("-",self)
        self._mul=QPushButton("x",self)
        self._div=QPushButton("/",self)
        self._eq=QPushButton("=",self)
        self._clear=QPushButton("C",self)
        self._del=QPushButton("DEL",self)
        self._dot=QPushButton(".",self)
        self._plus_minus=QPushButton("+/-",self)
        self._cross=QPushButton("❎",self)
        self.result=QLabel("0",self)
        self.search=QLabel(self)

        l.addWidget(self.search)
        l.addWidget(self.result)

        h=QHBoxLayout()
        h.addWidget(self._del)
        h.addWidget(self._clear)
        h.addWidget(self._div)
        h.addWidget(self._cross)
        l.addLayout(h)

        h=QHBoxLayout()
        h.addWidget(self._1)
        h.addWidget(self._2)
        h.addWidget(self._3)
        h.addWidget(self._add)
        l.addLayout(h)

        h=QHBoxLayout()
        h.addWidget(self._4)
        h.addWidget(self._5)
        h.addWidget(self._6)
        h.addWidget(self._sub)
        l.addLayout(h)

        h=QHBoxLayout()
        h.addWidget(self._7)
        h.addWidget(self._8)
        h.addWidget(self._9)
        h.addWidget(self._mul)
        l.addLayout(h)

        h=QHBoxLayout()
        h.addWidget(self._plus_minus)
        h.addWidget(self._0)
        h.addWidget(self._dot)
        h.addWidget(self._eq)
        l.addLayout(h)

        self.setLayout(l)

        self.search.setAlignment(Qt.AlignRight)
        self.result.setAlignment(Qt.AlignRight)
        self.search.setObjectName("search")
        self.result.setObjectName("result")
        
        self.setStyleSheet("""
                            QPushButton{
                           font-size:20px;
                           font-family:Cambria;
                           background-color: #f0f0f0;

                           }
                           QLabel{
                            font-family:arial;
                           }
                           QLabel#search{
                           font-size:25px;
                           color:grey;
                           }
                           QLabel#result{
                           font-size:70px;
                           font-weight : bold ;
                           }
                           
                            """)
        
        self._1.clicked.connect(self.operators)
        self._2.clicked.connect(self.operators)
        self._3.clicked.connect(self.operators)
        self._4.clicked.connect(self.operators)
        self._5.clicked.connect(self.operators)
        self._6.clicked.connect(self.operators)
        self._7.clicked.connect(self.operators)
        self._8.clicked.connect(self.operators)
        self._9.clicked.connect(self.operators)
        self._0.clicked.connect(self.operators)
        self._dot.clicked.connect(self.operators)
        self._add.clicked.connect(self.re)
        self._sub.clicked.connect(self.re)
        self._mul.clicked.connect(self.re)
        self._div.clicked.connect(self.re)
        # self._minus.clicked.connect(self.operators)
        self._eq.clicked.connect(self.ans)

    

    def operators(self):
        click_button=self.sender()
        self.r+=click_button.text()
        self.result.setText(self.r)

    def re(self):
        self.r+=self.sender().text()
        self.search.setText(self.r)
        self.r=""
        self.result.setText(self.r)

    def ans(self):
        c=self.search.text()
        d=self.result.text()
        if c[-1]=="+":
            self.result.setText(str(int(d)+int(c[:-1])))
        elif c[-1]=="-":
            self.result.setText(str(int(d)-int(c[:-1])))
        elif c[-1]=="*":
            self.result.setText(str(int(d)*int(c[:-1])))
        elif c[-1]=="/":
            self.result.setText(str(int(d)/int(c[:-1])))

        

def main():
    app = QApplication(sys.argv)
    window = calculator()
    window.show()
    sys.exit(app.exec_())

if __name__=="__main__":
    main()