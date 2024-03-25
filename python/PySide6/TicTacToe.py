from EasyDev13 import Menu
from game14 import GameWindow
from PySide6.QtWidgets import QApplication

class TicTacToe:
    def __init__(self):
        self.menu = Menu()
        self.game = GameWindow()

        self.menu.setup_ui()

        self.menu.boton_jugar.clicked.connect(self.abrir_juego)

    def abrir_juego(self):
        self.menu.hide()
        self.game.setup_ui()
        self.game.show()


import sys

app = QApplication(sys.argv)

main = TicTacToe()
main.menu.show()

sys.exit(app.exec())