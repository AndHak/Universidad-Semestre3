from PySide6.QtWidgets import *
from PySide6.QtCore import *

class Main(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        self.setup_form()

    def setup_form(self):
        self.stack = QStackedLayout()

        

        self.setLayout(self.stack)


if __name__ == "__main__":
    app = QApplication([])
    window = Main()
    window.show()
    app.exec()
