from PySide6.QtCore import *
from PySide6.QtWidgets import *

from Estilos13 import *

class GameWindow(QMainWindow):

    current_player = "X"
    x_moves = set()
    o_moves = set()
    winner_moves = [
        #Horizontal
        {"11", "12", "13"},
        {"21", "22", "23"},
        {"31", "32", "33"},

        #Vertical
        {"11", "21", "31"},
        {"12", "22", "32"},
        {"13", "23", "33"},

        #Diagonal
        {"11", "22", "33"},
        {"13", "22", "31"}
    ]

    def setup_ui(self):
        self.resize(QSize(600, 600))

        self.frame_titulo = QFrame()
        self.frame_buttons = QFrame()

        self.root_layout = QVBoxLayout()
        self.root_layout.addWidget(self.frame_titulo, 30)
        self.root_layout.addWidget(self.frame_buttons, 70)

        self.widget = QWidget()
        self.widget.setLayout(self.root_layout)
 
        self.setCentralWidget(self.widget)
        self.setup_buttons_frame()
        self.setStyleSheet(estilos_juego)
        
    def setup_titulo_frame(self, player_1, player_2):
        self.titulo_principal = QLabel(f"{player_1} VS {player_2}", objectName="titulo_principal")

        self.titulo_principal.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)

        self.titulo_principal_layout = QVBoxLayout()

        self.titulo_principal_layout.addWidget(self.titulo_principal)

        self.frame_titulo.setLayout(self.titulo_principal_layout)

    def add_button_to_layout(self, i, j):
        coordinates = f"{i}{j}"
        button = QPushButton()
        button.clicked.connect(lambda: self.record_move(coordinates, button))
        self.buttons_layout.addWidget(button, i, j)
        

    def setup_buttons_frame(self):

        self.buttons_layout = QGridLayout()
        
        for i in range(1, 4):
            for j in range(1, 4):
                self.add_button_to_layout(i, j)

        self.frame_buttons.setLayout(self.buttons_layout)

    def record_move(self, coordinates, button):
        button.setText(self.current_player)
        button.setEnabled(False)
        if (self.current_player == "X"):
            self.x_moves.add(coordinates)
            self.current_player = "O"
            self.verify_moves()
        else:
            self.o_moves.add(coordinates)
            self.current_player = "X"
            self.verify_moves()
        print("click en", coordinates)

    def verify_moves(self):
        if self.current_player == "X":
            player_moves = self.x_moves
        else:
            player_moves = self.o_moves

        for move in self.winner_moves:
            if move.issubset(player_moves):
                print(self.current_player, "Has ganado")
        


import sys

app = QApplication(sys.argv)

menu = GameWindow()
menu.setup_ui()
menu.show()

sys.exit(app.exec())