import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("pb.ui")[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb1.clicked.connent(self.button1Function)
        self.pb2.clicked.connent(self.button2Function)

    def button1Function(self):
        print("pb1 Clicked")

    def button2Fuction(self):
        print("pb2 Clicked")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
