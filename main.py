from ast import Del, Global
import csv
import os
from unicodedata import name
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

pretempname = None

itemname = None

if os.system == "nt":
    path = "Bookmarks\\"
else:
    path = "Bookmarks/"

print(path)

list = []

deenabled = 0

def loadlist():
    filelist = os.listdir("Bookmarks")
    for i in range(len(filelist)):
        filelist[i] = filelist[i].replace('.csv', '')
        print(filelist[i])
    for i in filelist:
        print(i)
        bookmarksscreen.Blist.addItem(i)

def duplicatefound():
    duplicatescreen.show()

def checkforduplicates():
    filelist = os.listdir("Bookmarks")
    for i in range(len(filelist)):
        filelist[i] = filelist[i].replace('.csv', '')
    for i in range(len(filelist)):
        if tempname == filelist[i]:
            return 1
    print(filelist)
    return 0

def deleteitem():
    print(itemname)
    os.remove(f'{path}{itemname}.csv')
    current = bookmarksscreen.Blist.currentRow()
    bookmarksscreen.Blist.takeItem(current)
    disabledeleteandeditafterdelete()
    deleteconfirmationscreen.close()

def writebookmark():
    global tempname
    open(f'{path}{tempname}.csv', 'w', newline = "")

def disabledeleteandeditafterdelete():
    global deenabled
    bookmarksscreen.Delete.setEnabled(False)
    bookmarksscreen.Edit.setEnabled(False)
    deenabled = bookmarksscreen.Blist.currentRow()

def addtolist():
    global tempname
    if tempname != "":
        bookmarksscreen.Blist.addItem(tempname)
    writebookmark()

def reset():
    bnamescreen.Nameinput.setText("")

class Mainscreen(QMainWindow):
    def __init__(self):
        super(Mainscreen, self).__init__()
        loadUi('mainscreen.ui', self)
        widget.setWindowIcon(QIcon("icon.png"))
        widget.setWindowTitle("unamed")
        self.Bookmarks.clicked.connect(self.gotobookmarks)
        self.Bookmarks.clicked.connect(loadlist)

    def gotobookmarks(self):
        widget.addWidget(bookmarksscreen)
        widget.removeWidget(mainscreen)
        # widget.setCurrentIndex(widget.currentIndex()+1)

class Bookmarksscreen(QMainWindow):
    def __init__(self):
        super(Bookmarksscreen, self).__init__()
        loadUi('bookmarksscreen.ui', self)
        self.Main.clicked.connect(self.gotomain)
        self.Add.clicked.connect(self.gotoname)
        self.Blist.itemSelectionChanged.connect(self.disabledeleteandedit)
        self.Blist.itemClicked.connect(self.enabledeleteandedit)
        self.Delete.clicked.connect(self.deleteitem)
        
    def disabledeleteandedit(self):
        global deenabled
        if deenabled == self.Blist.currentRow():
            self.Delete.setEnabled(False)
            self.Edit.setEnabled(False)
        

    def enabledeleteandedit(self):
        global deenabled, itemname
        self.Delete.setEnabled(True)
        self.Edit.setEnabled(True)
        print(self.Blist.currentItem().text())
        deenabled = self.Blist.currentRow()
        itemname = self.Blist.currentItem().text()

    def gotoname(self):
        bnamescreen.show()

    def gotomain(self):
        widget.addWidget(mainscreen)
        widget.removeWidget(bookmarksscreen)
        # widget.setCurrentIndex(widget.currentIndex()+1)
    
    def deleteitem(self):
        deleteconfirmationscreen.show()

    def disabledeleteandedit(self):
        self.Delete.setEnabled(False)
        self.Edit.setEnabled(False)

class Bnamescreen(QMainWindow):
    def __init__(self):
        super(Bnamescreen, self).__init__()
        loadUi('bname.ui', self)
        self.setWindowIcon(QIcon("icon.png"))
        self.setWindowTitle("name")
        self.Confirm.clicked.connect(self.addname)
        self.Confirm.clicked.connect(self.close)
        self.setWindowTitle("name")
    
    def addname(self):
        global tempname
        tempname = self.Nameinput.text()
        allowit = 0
        allowit = checkforduplicates()
        if allowit == 0:
            pretempname = self.Nameinput.text()
            tempname = pretempname
            list.append(tempname)
            print(list)
            print(tempname)
            self.Nameinput.setText("")
            addtolist()
        else:
            duplicatefound()
        
class Duplicatescreen(QMainWindow):
    def __init__(self):
        super(Duplicatescreen, self).__init__()
        loadUi('duplicateerror.ui', self)
        self.setWindowIcon(QIcon("error.png"))
        self.setWindowTitle("Error")
        self.pushButton.clicked.connect(self.close)
        self.pushButton.clicked.connect(reset)
    
class Deleteconfirmationscreen(QMainWindow):
    def __init__(self):
        super(Deleteconfirmationscreen, self).__init__()
        loadUi('deletewarning.ui', self)
        self.setWindowIcon(QIcon("warning.png"))
        self.setWindowTitle("Are you sure?")
        self.OK.clicked.connect(deleteitem)
        self.Cancel.clicked.connect(self.close)


   
app = QApplication(sys.argv)
widget = QStackedWidget()
bnamescreen = Bnamescreen()
mainscreen = Mainscreen()
bookmarksscreen = Bookmarksscreen()
duplicatescreen = Duplicatescreen()
deleteconfirmationscreen = Deleteconfirmationscreen()
widget.addWidget(mainscreen)
widget.addWidget(bookmarksscreen)
bnamescreen.setFixedHeight(50)
bnamescreen.setFixedWidth(500)
duplicatescreen.setFixedHeight(110)
duplicatescreen.setFixedWidth(270)
deleteconfirmationscreen.setFixedHeight(110)
deleteconfirmationscreen.setFixedWidth(350)
widget.show()
sys.exit(app.exec())   
