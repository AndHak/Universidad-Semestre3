from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *


class Main(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        self.setup_form()

    def setup_form(self):
        form_layaout = QFormLayout()

        form_layaout.addRow("Name:", QLineEdit())
        form_layaout.addRow("Email:", QLineEdit())
        form_layaout.addRow("Age:", QLineEdit())

        self.setLayout(form_layaout)


if __name__=="__main__":
    app = QApplication()
    window = Main()
    window.show()
    app.exec()