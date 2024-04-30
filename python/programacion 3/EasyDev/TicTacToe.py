from PySide6.QtCore import *
from PySide6.QtWidgets import *
from python.PySide6.EasyDev.menu import Menu
from python.PySide6.EasyDev.game import GameWindow

class Controller(QObject):
    def __init__(self, menu):
        super().__init__()
        self.menu = menu

    def show_game_window(self):
        # Mostrar la ventana del juego
        self.game = GameWindow()
        self.game.setup_ui()
        self.game.show()

        # Cerrar la ventana del menú
        self.menu.close()

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    menu = Menu()
    controller = Controller(menu)
    menu.setup_ui(controller)
    menu.show()
    sys.exit(app.exec_())
