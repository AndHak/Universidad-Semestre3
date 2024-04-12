from PySide6.QtWidgets import *
from PySide6.QtGui import *
import random
import os
import sys

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.basedir = os.path.dirname(__file__)

        self.resize(500, 300)

        self.palabras = ["COMUNIDAD", "RESPONSABILIDAD", "CARRO", "FUTBOL", "ARMARIO", "TELEVISOR", "CONCIERTO", "CANTANTE", "CELULAR", "COMPUTADOR"]
        self.palabra = random.choice(self.palabras)
        self.letras_correctas = []
        self.letras_totales = ["_" for _ in range(len(self.palabra))]
        
        self.fallos = 0

        self.initUI()

    def initUI(self):
        papa_layout = QVBoxLayout(self)
        self.setLayout(papa_layout)

        contador = 1

        sub_layouts = []
        for i in range(3):
            sub_layout = QHBoxLayout()
            sub_layouts.append(sub_layout)
            papa_layout.addLayout(sub_layout)
            
            if i == 0:
                colors = ["red", "yellow"]
                for j, color in enumerate(colors):
                    self.label_image = QLabel()
                    self.label_palabra = QLabel()
                    if j == 1:
                        if self.fallos == 0:
                            ahor0 = r"python\programacion 3\images\ahorcado0.png"
                            self.label_image.setPixmap(ahor0)
                        sub_layout.addWidget(self.label_image)
                    elif j == 2:
                        self.label_palabra.setText(self.letras_totales)
                        sub_layout.addWidget(self.label_palabra)
                    contador += 1
                        
                        
            elif i == 1:
                colors = ["red", "yellow"]
                for j, color in enumerate(colors):
                    self.label_ingresar_letra = QLabel()
                    self.label_ingresar_letra.setText("Ingresar letra")
                    letra_line = QLineEdit()
                    if j == 1:
                        sub_layout.addWidget(self.label_ingresar_letra)
                    elif j == 2:
                        self.letra_line.setGeometry(0, 0, 10, 10)
                        sub_layout.addWidget(self.letra_line)
                    contador += 1
                contador += 1

            elif i == 2:
                colors = ["red", "yellow"]
                for j, color in enumerate(colors):
                    self.boton = QPushButton()
                    self.label_congrats = QLabel()
                    if j == 1:
                        sub_layout.addWidget(self.boton)
                    elif j == 2:
                        sub_layout.addWidget(self.label_congrats)
                    contador += 1
                contador += 1

        resultado = ""
        for letra in self.palabra:
            if letra in self.letras_correctas:
                resultado += letra
            else:
                resultado += "_"
        self.word_label.setText(resultado)

    def check_letter(self):
        letra_usuario = self.input_text.text().upper()
        letra = letra_usuario.upper()

        self.letras_totales += letra
        if letra not in self.palabra:
            self.fallos += 1
        else:
            self.letras_correctas += letra

        self.input_text.clear()
        self.update_display()

        if self.fallos >= 6:
            self.label_congrats.setText("Game Over!")
            self.label_congrats.setStyleSheet("font-family: Gameplay;")
            
            self.boton.setText("Nueva palabra")
            self.reset_game()

        if self.letras_correctas == self.palabra:
            self.label_congrats.setText("Congratulations")
            self.label_congrats.setStyleSheet("font-family: Gameplay;")

            self.boton.setText("Nueva palabra")
            self.reset_game()
            

    def reset_game(self):
        self.palabra = random.choice(self.palabras)
        self.boton.setText("Enviar")
        self.letras_correctas = ""
        self.letras_totales = ""
        self.fallos = 0

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec_())
