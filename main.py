from ast import Del, Global
import csv
from logging import BASIC_FORMAT
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

# DECLERATION DECLERATION
tempname = None
pretempname = None
itemname = None
deenabled = 0
card = []
bookmark = []
tempfront = None
tempback = None
# OTHER SYSTEMS INTERGRATION
if os.system == "nt":
    path = "Bookmarks\\"
    assets = "uisandassets\\"
else:
    path = "Bookmarks/"
    assets = "uisandassets/"

# OPENING NEW WINDOWS
def duplicatefound():
    duplicatescreen.show()

def openedit():
    # bookmark = []
    editbookmarksscreen.show()
    currentbookmark = open(f'{path}{bookmarksscreen.Blist.currentItem().text()}.csv', 'r+', encoding="utf8", newline="")
    # writer = csv.writer(currentbookmark)
    currentbookmark.close()

def gotoname():
    bnamescreen.show()
    bnamescreen.Nameinput.setText("")

# BOOKMARKSCREENLIST DEFS
def loadlist():
    filelist = os.listdir("Bookmarks")
    for i in range(len(filelist)):
        filelist[i] = filelist[i].replace('.csv', '')
        print(filelist[i])
    for i in filelist:
        print(i)
        bookmarksscreen.Blist.addItem(i)

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

# BOOKMARKS EDITING DEFS
def openbfront():
    bfrontscreen.show()

def addfront():
    global tempfront
    tempfront = bfrontscreen.Nameinput.text()
    while True:
        if tempfront != "":
            break
    editbookmarksscreen.Front.addItem(tempfront)
    bfrontscreen.close()
    bbackscreen.show()

def addback():
    global tempback
    tempback = bbackscreen.Nameinput.text()
    while True:
        if tempback != "":
            break
    editbookmarksscreen.Back.addItem(tempback)
    bbackscreen.close()
# OTHER DEFS
def reset():
    bnamescreen.Nameinput.setText("")



class Mainscreen(QMainWindow):
    def __init__(self):
        super(Mainscreen, self).__init__()
        loadUi(f'{assets}mainscreen.ui', self)
        widget.setWindowIcon(QIcon(f'{assets}icon.png'))
        widget.setWindowTitle("unamed")
        self.Bookmarks.clicked.connect(self.gotobookmarks)
        self.Bookmarks.clicked.connect(loadlist)

    def gotobookmarks(self):
        widget.addWidget(bookmarksscreen)
        widget.removeWidget(mainscreen)
        widget.removeWidget(bfrontscreen)
        widget.removeWidget(bbackscreen)

class Bookmarksscreen(QMainWindow):
    def __init__(self):
        super(Bookmarksscreen, self).__init__()
        loadUi(f'{assets}bookmarksscreen.ui', self)
        self.Main.clicked.connect(self.gotomain)
        self.Add.clicked.connect(gotoname)
        self.Blist.itemSelectionChanged.connect(self.disabledeleteandedit)
        self.Blist.itemClicked.connect(self.enabledeleteandedit)
        self.Delete.clicked.connect(self.deleteitem)
        self.Edit.clicked.connect(openedit)
        
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

    def gotomain(self):
        self.Blist.clear()
        print("cleared")
        widget.addWidget(mainscreen)
        widget.removeWidget(bookmarksscreen)
        widget.removeWidget(bfrontscreen)
        widget.removeWidget(bbackscreen)
    
    def deleteitem(self):
        deleteconfirmationscreen.show()

    def disabledeleteandedit(self):
        self.Delete.setEnabled(False)
        self.Edit.setEnabled(False)

#POP UP SCREENS
class Bnamescreen(QMainWindow):
    def __init__(self):
        super(Bnamescreen, self).__init__()
        loadUi(f'{assets}bname.ui', self)
        self.setWindowIcon(QIcon(f'{assets}icon.png'))
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
            print(tempname)
            self.Nameinput.setText("")
            addtolist()
        else:
            duplicatefound()
        
class Duplicatescreen(QMainWindow):
    def __init__(self):
        super(Duplicatescreen, self).__init__()
        loadUi(f'{assets}duplicateerror.ui', self)
        self.setWindowIcon(QIcon(f'{assets}icon.png'))
        self.setWindowTitle("Error")
        self.pushButton.clicked.connect(self.close)
        self.pushButton.clicked.connect(reset)
    
class Deleteconfirmationscreen(QMainWindow):
    def __init__(self):
        super(Deleteconfirmationscreen, self).__init__()
        loadUi(f'{assets}deletewarning.ui', self)
        self.setWindowIcon(QIcon(f'{assets}icon.png'))
        self.setWindowTitle("Are you sure?")
        self.OK.clicked.connect(deleteitem)
        self.Cancel.clicked.connect(self.close)

class Bfrontscreen(QMainWindow):
    def __init__(self):
        super(Bfrontscreen, self).__init__()
        loadUi(f'{assets}bfront.ui', self)
        self.setWindowIcon(QIcon(f'{assets}icon.png'))
        self.setWindowTitle("Edit")
        self.Confirm.clicked.connect(addfront)

class Bbackscreen(QMainWindow):
    def __init__(self):
        super(Bbackscreen, self).__init__()
        loadUi(f'{assets}bback.ui', self)
        self.setWindowIcon(QIcon(f'{assets}icon.png'))
        self.setWindowTitle("Edit")
        self.Confirm.clicked.connect(addback)

class Editbookmarksscreen(QMainWindow):
    def __init__(self):
        super(Editbookmarksscreen, self).__init__()
        loadUi(f'{assets}bookmarksedit.ui', self)
        self.resize(600, 450)
        self.setWindowIcon(QIcon(f'{assets}icon.png'))
        self.setWindowTitle("Edit")
        self.Add.clicked.connect(openbfront)


app = QApplication(sys.argv)
widget = QStackedWidget()

bnamescreen = Bnamescreen()
mainscreen = Mainscreen()
bookmarksscreen = Bookmarksscreen()
duplicatescreen = Duplicatescreen()
deleteconfirmationscreen = Deleteconfirmationscreen()
editbookmarksscreen = Editbookmarksscreen()
bfrontscreen = Bfrontscreen()
bbackscreen = Bbackscreen()

widget.addWidget(mainscreen)
widget.addWidget(bookmarksscreen)

bnamescreen.setFixedHeight(50)
bnamescreen.setFixedWidth(500)
bfrontscreen.setFixedHeight(80)
bfrontscreen.setFixedWidth(330)
bbackscreen.setFixedHeight(80)
bbackscreen.setFixedWidth(330)
duplicatescreen.setFixedHeight(110)
duplicatescreen.setFixedWidth(280)
deleteconfirmationscreen.setFixedHeight(110)
deleteconfirmationscreen.setFixedWidth(350)
widget.show()
sys.exit(app.exec())   
