from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *
import sys
import os

class MainWindow(QMainWindow):
    basedir = os.path.dirname(__file__)
    score_x = 0
    score_o = 0

    current_player = "X"

    player_o = None
    player_x = None

    allmoves = [[0,0,0],
               [0,0,0],
               [0,0,0]]
    


    x_icon = os.path.join(basedir, "images/x_icon.png")
    o_icon = os.path.join(basedir, "images/o_icon.png")

    def __init__(self):
        super().__init__()


        self.setWindowTitle("Tic Tac Toe")
        self.icon_window = QPixmap(os.path.join(self.basedir, "images/Tic_tac_toe.png"))
        self.setWindowIcon(self.icon_window)
        self.resize(QSize(400, 600))

        self.imagen_x = QPixmap(self.x_icon)
        self.imagen_o = QPixmap(self.o_icon)

        self.setup_ui()

    def setup_ui(self):
        self.root_layout = QVBoxLayout()

        self.frame_principal = QFrame()
        self.root_layout.addWidget(self.frame_principal)

        self.stacked_layout = QStackedLayout(self.frame_principal)
        self.pagina_1()
        self.pagina_2()
        self.pagina_3()

        self.main_widget = QWidget()
        self.main_widget.setLayout(self.root_layout)
        self.setCentralWidget(self.main_widget)

    def pagina_1(self):
        self.root_pagina1 = QVBoxLayout()

        self.frame_imagen = QFrame()
        self.frame_titulo = QFrame()
        self.frame_entradas = QFrame()
        self.frame_boton = QFrame()
        self.layout_imagen = QHBoxLayout()
        self.layout_titulo = QVBoxLayout()
        self.layout_entradas = QFormLayout()
        self.layout_boton = QVBoxLayout()

        self.root_pagina1.addWidget(self.frame_imagen, 35)
        self.root_pagina1.addWidget(self.frame_titulo, 10)
        self.root_pagina1.addWidget(self.frame_entradas, 50)
        self.root_pagina1.addWidget(self.frame_boton, 5)


        # Photo
        image_path = os.path.join(self.basedir, 'images/Tic_tac_toe.png')
        self.imagen = QPixmap(image_path)
        self.label_foto = QLabel(self)
        self.imagen = self.imagen.scaled(140, 190, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.label_foto.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.label_foto.setPixmap(self.imagen)

        self.layout_imagen.addWidget(self.label_foto)
        self.frame_imagen.setLayout(self.layout_imagen)


        #Titulo
        self.title_game = QLabel()
        self.title_game.setText("Tic Tac Toe")
        self.title_game.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        self.layout_titulo.addWidget(self.title_game)
        self.frame_titulo.setLayout(self.layout_titulo)


        #Entradas
        self.label_jugador_x = QLabel("Jugador X")
        self.line_edit_jugador_x = QLineEdit()
        self.label_jugador_o = QLabel("Jugador O")
        self.line_edit_jugador_o = QLineEdit()
        self.error_label = QLabel()
        
        self.layout_entradas.addRow(self.label_jugador_x, self.line_edit_jugador_x)
        self.layout_entradas.addRow(self.label_jugador_o, self.line_edit_jugador_o)
        self.layout_entradas.addWidget(self.error_label)
        self.frame_entradas.setLayout(self.layout_entradas)


        # Button Jugar
        self.button_jugar = QPushButton("Jugar")
        self.button_jugar.clicked.connect(self.show_pagina_2)
        self.layout_boton.addStretch(1)
        self.layout_boton.addWidget(self.button_jugar)
        self.frame_boton.setLayout(self.layout_boton)

        self.pagina1 = QWidget()
        self.pagina1.setLayout(self.root_pagina1)
        self.stacked_layout.addWidget(self.pagina1)


    def pagina_2(self):
        self.root_pagina2 = QVBoxLayout()

        self.info_players_layout = QHBoxLayout()
        self.buttons_game_layout = QGridLayout()
        self.button_group_layout = QHBoxLayout()
        self.frame_info_players = QFrame()
        self.frame_buttons_game = QFrame()
        self.frame_button_group = QFrame()

        self.root_pagina2.addWidget(self.frame_info_players, 30)
        self.root_pagina2.addWidget(self.frame_buttons_game, 65)
        self.root_pagina2.addWidget(self.frame_button_group, 5)

        #Info players
        self.player_one_layout = QVBoxLayout()
        self.vs_label_layout = QVBoxLayout()
        self.vs_label_layout.setAlignment(Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignHCenter)
        self.player_two_layout = QVBoxLayout()

        # Etiquetas para los nombres de los jugadores y puntuaciones
        self.label_player_one = QLabel()
        self.label_player_one.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_player_one.setStyleSheet("""
                                            color: red;
                                            font-size: 20px;""")
        self.label_player_two = QLabel()
        self.label_player_two.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_player_two.setStyleSheet("""
                                            color: blue;
                                            font-size: 20px;""")


        self.score_player_one = QLabel()
        self.score_player_one.setText(f"{self.score_x}")
        self.score_player_one.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.score_player_one.setStyleSheet("font-size: 20px;")

        self.score_player_two = QLabel()
        self.score_player_two.setText(f"{self.score_o}")
        self.score_player_two.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.score_player_two.setStyleSheet("font-size: 20px;")

        # Agregar elementos a los layouts correspondientes
        self.player_one_layout.addWidget(self.label_player_one)
        self.player_one_layout.addWidget(self.score_player_one)

        self.tictactoe_label = QLabel("TIC TAC TOE")
        self.tictactoe_label.setStyleSheet("""
                                    font-size: 16px;""")
        self.vs_label_layout.addWidget(self.tictactoe_label)
        self.tictactoe_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.vs_label = QLabel("VS")
        self.vs_label_layout.addWidget(self.vs_label)
        self.vs_label.setStyleSheet("""
                                    font-size: 20px;""")
        
        self.vs_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.winner_player = QLabel()
        self.vs_label_layout.addWidget(self.winner_player)
        self.winner_player.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.winner_player.setStyleSheet("font-size: 16px;")
        self.winner_player.setText(f"En Turno: {self.player_x} - {self.current_player}")



        self.player_two_layout.addWidget(self.label_player_two)
        self.player_two_layout.addWidget(self.score_player_two)

        self.info_players_layout.addLayout(self.player_one_layout)
        self.info_players_layout.addLayout(self.vs_label_layout)
        self.info_players_layout.addLayout(self.player_two_layout)

        self.frame_info_players.setLayout(self.info_players_layout)
        ####

        #Grid tictactoe
        for i in range(1, 4):
            for j in range(1, 4):
                self.crear_boton(i,j)

        self.frame_buttons_game.setLayout(self.buttons_game_layout)

        #Boton group y reload
        self.boton_volver_layaout = QHBoxLayout()

        self.back_button = QPushButton()
        self.back_button.clicked.connect(self.volver)
        image_back = os.path.join(self.basedir, "images/volver.png")
        self.imagen_volver = QPixmap(image_back)
        self.back_button.setIcon(self.imagen_volver)
        self.boton_volver_layaout.addWidget(self.back_button)


        self.boton_volver_layaout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.button_group_layout.addLayout(self.boton_volver_layaout)



        #Info y rety
        self.botones_info_retry = QHBoxLayout()

        self.button_group_layout.addLayout(self.botones_info_retry)

        self.reload_button = QPushButton()
        self.reload_button.clicked.connect(self.recargar)
        image_reload = os.path.join(self.basedir, "images/reload.png")
        self.imagen_reload = QPixmap(image_reload)
        self.reload_button.setIcon(self.imagen_reload)
        self.botones_info_retry.addWidget(self.reload_button)

        self.button_group = QPushButton()
        self.button_group.clicked.connect(self.show_pagina_3)
        image_group = os.path.join(self.basedir, 'images/grupo.png')
        self.imagen_group = QPixmap(image_group)
        self.button_group.setIcon(self.imagen_group)
        self.botones_info_retry.addWidget(self.button_group)


        self.botones_info_retry.setAlignment(Qt.AlignmentFlag.AlignRight)
 
        self.frame_button_group.setLayout(self.button_group_layout)

   
        


        self.pagina2 = QWidget()
        self.pagina2.setLayout(self.root_pagina2)
        self.stacked_layout.addWidget(self.pagina2)

    def mostrar_en_turno(self):
        if self.current_player == "X":
            self.player_x = self.line_edit_jugador_x.text()
            self.winner_player.setText(f"En Turno: {self.player_x}  [X]")
        if self.current_player == "O":
            self.player_x = self.line_edit_jugador_o.text()
            self.winner_player.setText(f"En Turno: {self.player_o}  [O]")

    
    def crear_boton(self, i, j):
        coordinates = f"{i}{j}"
        button_game = QPushButton()
        button_game.setStyleSheet("""
                                background-color: #2C2C2C;
                                border: none;
                                  """)
        button_game.setMinimumSize(70, 70) 
        button_game.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding) 
        button_game.setIconSize(QSize(100, 100)) 
        button_game.setEnabled(True) 
        button_game.setProperty("isUsed", False)
        self.buttons_game_layout.addWidget(button_game, i, j)
        button_game.clicked.connect(lambda: self.record_move(coordinates, button_game))
        

                
    def record_move(self, coordinates, button):
        if not button.property("isUsed"):
            self.mostrar_en_turno()
            i, j = int(coordinates[0]) - 1, int(coordinates[1]) - 1
            button.setIcon(self.imagen_x if self.current_player == "X" else self.imagen_o)
            button.setProperty("isUsed", True)
            if self.current_player == "X":
                self.allmoves[i][j] = 1
                self.verify_moves(self.player_x)
                self.current_player = "O"
            else:
                self.allmoves[i][j] = 4
                self.verify_moves(self.player_o)
                self.current_player = "X"

            
    def verify_moves(self, player):
        #Si es X se escoge la matriz de X y el texto del jugador
        player_moves = self.allmoves
        if self.current_player == "X":
            player = self.label_player_one.text()
        #de lo contrario lo mismo para el otro jugador
        else:
            player = self.label_player_two.text()

        #Recorremos el numero de filas de la matriz
        for i in range(3):

            #checar la suma de los valores de la fila
            if sum(player_moves[i]) == 3 or sum(player_moves[i]) == 12:
                self.declare_winner(player)

            #Para j = 0 de la misma fila i, para j = 1, para j = 2
            if player_moves[0][i] + player_moves[1][i] + player_moves[2][i] == 3 or player_moves[0][i] + player_moves[1][i] + player_moves[2][i] == 12:
                self.declare_winner(player)

        #Chekar la diagonal principal
        if player_moves[0][0] + player_moves[1][1] + player_moves[2][2] == 3 or player_moves[0][0] + player_moves[1][1] + player_moves[2][2] == 12:
            self.declare_winner(player)
        
        #Chekar la diagonal secundaria
        if player_moves[0][2] + player_moves[1][1] + player_moves[2][0] == 3 or player_moves[0][2] + player_moves[1][1] + player_moves[2][0] == 12:
            self.declare_winner(player)


    def declare_winner(self, player):
        self.winner_player.setText(f"Ganador: {player}")
        if self.current_player == "X":
            self.score_x += 1
            self.score_player_one.setText(str(self.score_x))
        else:
            self.score_o += 1
            self.score_player_two.setText(str(self.score_o))
        self.disable_all_buttons()

    def disable_all_buttons(self):
        for button in self.frame_buttons_game.findChildren(QPushButton):
            button.setProperty("isUsed", True)

    def recargar(self):
        self.allmoves = [[0,0,0],
               [0,0,0],
               [0,0,0]]



        self.winner_player.clear()
        self.mostrar_en_turno()

        for button in self.frame_buttons_game.findChildren(QPushButton):
            button.setIcon(QIcon()) 
            button.setProperty("isUsed", False) 
            button.setEnabled(True)

        self.show_pagina_2

    def volver(self):
        self.show_pagina_1()
        self.allmoves = [[0,0,0],
               [0,0,0],
               [0,0,0]]
        
        self.score_x = 0
        self.score_o = 0
        self.current_player = "X"
        self.player_o = None
        self.player_x = None
        self.line_edit_jugador_o.setText("")
        self.line_edit_jugador_x.setText("")

        self.winner_player.clear()
        for button in self.frame_buttons_game.findChildren(QPushButton):
            button.setIcon(QIcon()) 
            button.setProperty("isUsed", False) 
            button.setEnabled(True)


    def pagina_3(self):
        self.root_pagina3 = QVBoxLayout()

        self.info_creator_layout = QVBoxLayout()
        self.button_back_layout = QHBoxLayout()
        self.frame_creator = QFrame()
        self.frame_back = QFrame()

        self.root_pagina3.addWidget(self.frame_creator, 95)
        self.root_pagina3.addWidget(self.frame_back, 5)

        # Creator info
        image_path = os.path.join(self.basedir, 'images/yo.jpeg')
        self.imagen = QPixmap(image_path)
        self.label_foto = QLabel(self)
        self.imagen = self.imagen.scaled(140, 190, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.label_foto.setAlignment(Qt.AlignmentFlag.AlignCenter) 
        self.label_foto.setPixmap(self.imagen)

        self.created_by = QLabel()
        self.created_by.setText("By")
        self.created_by.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.created_by_name = QLabel()
        self.created_by_name.setText("Andres Guerra")
        self.created_by_name.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.info_creator_layout.addWidget(self.label_foto)
        self.info_creator_layout.addWidget(self.created_by)
        self.info_creator_layout.addWidget(self.created_by_name)
        self.info_creator_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.frame_creator.setLayout(self.info_creator_layout)

        # Boton group
        self.button_back = QPushButton()
        image_controller = os.path.join(self.basedir, 'images/controller.png')
        self.imagen_back = QPixmap(image_controller)
        self.button_back.setIcon(self.imagen_back)
        self.button_back.clicked.connect(self.show_pagina_2)

        self.button_back_layout.addWidget(self.button_back)
        self.button_back_layout.setAlignment(Qt.AlignmentFlag.AlignRight) 
        self.frame_back.setLayout(self.button_back_layout)

        self.pagina3 = QWidget()
        self.pagina3.setLayout(self.root_pagina3)
        self.stacked_layout.addWidget(self.pagina3)


    def show_pagina_1(self):
        self.stacked_layout.setCurrentIndex(0)

    def show_pagina_2(self):
        line_valido_x = self.line_edit_jugador_x.text().split()
        line_valido_o = self.line_edit_jugador_o.text().split()

        if not line_valido_x or not line_valido_o:
            if not line_valido_x and not line_valido_o:
                self.error_label.setText("Ingrese el nombre del jugador X y jugador O")
                return
            if not line_valido_x:
                self.error_label.setText("Ingrese el nombre del jugador X")
            if not line_valido_o:
                self.error_label.setText("Ingrese el nombre del jugador O")
        else:
            self.player_x = self.line_edit_jugador_x.text()
            self.player_o = self.line_edit_jugador_o.text()
            
            if self.player_x:
                self.label_player_one.setText(self.player_x)
            else:
                self.label_player_one.setText("Player X")
            
            if self.player_o:
                self.label_player_two.setText(self.player_o)
            else:
                self.label_player_two.setText("Player O")

            self.score_player_one.setText(str(self.score_x))
            self.score_player_two.setText(str(self.score_o))
            self.mostrar_en_turno()
            self.stacked_layout.setCurrentIndex(1)
    
    def show_pagina_3(self):
        self.stacked_layout.setCurrentIndex(2)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")

    window = MainWindow()
    window.show()
    sys.exit(app.exec())
