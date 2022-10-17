from PyQt6.QtWidgets import (
    QApplication, QWidget, QPushButton, QLabel,
    QLineEdit, QVBoxLayout, QGridLayout
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from PyQt6.uic import loadUi
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        # self.setWindowIcon(QIcon("utsu200-m.gif"))
        # self.setWindowTitle("鬱")

        # layout = QGridLayout()
        # self.setLayout(layout)

        # bookmarks = QPushButton("Bookmarks")
        # bookmarks.clicked.connect(ben)
        # layout.addWidget(bookmarks, 1, 0)
        loadUi("mainscreen.ui")


app = QApplication(sys.argv)
Window = Window()
Window.show()
sys.exit(app.exec())
