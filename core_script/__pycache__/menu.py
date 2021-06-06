import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget, QMenu
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize, QTimer
import os

class Example(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(320, 200))
        self.setWindowTitle("MathBot - VHCID.TECH")

        self.bt1 = QPushButton('Start Basic Calculation', self)
        self.bt2 = QPushButton('Start Areas Calculation', self)
        self.bt3 = QPushButton('Start Volume Calculation', self)
        self.bt4 = QPushButton('Start Surface Calculation', self)
        self.bt5 = QPushButton('Start Hypotenuse', self)
        self.bt6 = QPushButton('Turn Off', self)

        self.bt1.move(50, 50)
        self.bt2.move(50, 100)
        self.bt3.move(170, 100)
        self.bt4.move(170, 50)
        self.bt5.move(50, 150)
        self.bt6.move(170, 150)
        self.bt1.clicked.connect(self.Button1)
        self.count = 10
        self.bt2.clicked.connect(self.Button2)
        self.count = 10
        self.bt3.clicked.connect(self.Button3)
        self.count = 10
        self.bt4.clicked.connect(self.Button4)
        self.count = 10
        self.bt5.clicked.connect(self.Button5)
        self.count = 10
        self.bt6.clicked.connect(self.Button6)
        self.count = 10

    def Button1(self):
        os.system('python basic.py')
    def Button2(self):
        os.system('python areas.py')
    def Button3(self):
        os.system('python volume.py')
    def Button4(self):
        os.system('python surface-area.py')
    def Button5(self):
        os.system('python hypotenus.py')
    def Button6(self):
        exit()





if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = Example()
    mainWin.show()
    sys.exit(app.exec_())
