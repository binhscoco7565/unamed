from PyQt6.QtWidgets import (
    QApplication, QWidget, QPushButton, QLabel,
    QLineEdit, QVBoxLayout, QGridLayout, QDialog, QMainWindow, QStackedWidget
)

from PyQt6 import QtWidgets, uic
from PyQt6.uic import loadUi
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
import sys

class Mainscreen(QMainWindow):
    def __init__(self):
        super(Mainscreen, self).__init__()
        loadUi("mainscreen.ui", self)
        self.Bookmarks.clicked.connect(self.gotobookmarks)

    def gotobookmarks(self):
        bookmarksscreen = Bookmarksscreen()
        widget.addWidget(bookmarksscreen)
        widget.setCurrentIndex(widget.currentIndex()+1)

class Bookmarksscreen(QMainWindow):
    def __init__(self):
        super(Bookmarksscreen, self).__init__()
        loadUi("Simpleest.ui", self)

app = QApplication(sys.argv)
widget = QStackedWidget()
mainscreen = Mainscreen()
bookmarksscreen = Bookmarksscreen()
widget.addWidget(mainscreen)
widget.addWidget(bookmarksscreen)
widget.setFixedWidth(700)
widget.setFixedHeight(500)
widget.show()
sys.exit(app.exec())
