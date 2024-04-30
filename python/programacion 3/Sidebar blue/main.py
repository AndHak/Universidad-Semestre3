from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
import sys
from Sidebar import MySideBar

app = QApplication(sys.argv)

window = MySideBar()

window.show()
app.exec()