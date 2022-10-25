from ast import Global
from asyncio.windows_events import NULL
from PyQt6.QtWidgets import (
    QApplication, QWidget, QPushButton, QLabel,
    QLineEdit, QVBoxLayout, QGridLayout, QDialog, QMainWindow, QStackedWidget
)

from PyQt6 import QtWidgets, uic
from PyQt6.uic import loadUi
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
import sys

tempname = None

class Mainscreen(QMainWindow):
    def __init__(self):
        super(Mainscreen, self).__init__()
        loadUi("mainscreen.ui", self)
        widget.setWindowIcon(QIcon("icon.png"))
        widget.setWindowTitle("unamed")
        self.Bookmarks.clicked.connect(self.gotobookmarks)

    def gotobookmarks(self):
        widget.addWidget(bookmarksscreen)
        widget.removeWidget(mainscreen)
        # widget.setCurrentIndex(widget.currentIndex()+1)

class Bookmarksscreen(QMainWindow):
    def __init__(self):
        super(Bookmarksscreen, self).__init__()
        loadUi("bookmarksscreen.ui", self)
        self.Main.clicked.connect(self.gotomain)
        self.Add.clicked.connect(self.gotoname)

    def gotoname(self):
        bnamescreen.show()

    def gotomain(self):
        widget.addWidget(mainscreen)
        widget.removeWidget(bookmarksscreen)
        # widget.setCurrentIndex(widget.currentIndex()+1)

def addtolist():
    global tempname
    if tempname != "":
        bookmarksscreen.Blist.addItem(tempname)

class Bnamescreen(QMainWindow):
    def __init__(self):
        super(Bnamescreen, self).__init__()
        loadUi("bname.ui", self)
        self.setWindowIcon(QIcon("icon.png"))
        self.setWindowTitle("name")
        self.Confirm.clicked.connect(self.addname)
        self.Confirm.clicked.connect(self.close)
    
    def addname(self):
        global tempname
        tempname = self.Nameinput.text()
        print(tempname)
        self.Nameinput.setText("")
        addtolist()
        



app = QApplication(sys.argv)
widget = QStackedWidget()
bnamescreen = Bnamescreen()
mainscreen = Mainscreen()
bookmarksscreen = Bookmarksscreen()
widget.addWidget(mainscreen)
widget.addWidget(bookmarksscreen)
bnamescreen.setFixedHeight(50)
bnamescreen.setFixedWidth(500)
widget.show()
sys.exit(app.exec())
