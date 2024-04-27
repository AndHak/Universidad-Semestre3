##radiobutton se lo utiliza cuando tengo datos autoexcluyentes 
#si tengo a no puedo escoger b y viceversa

#setcheked ;podre verificar el estado del boton
#ischejked :permite verificar si un boton tiene la marca o no tipo bool
#settext : modifica el texto del boton
#text :

#señal de tipo toggled() on (encendico) off (apagadp)


##qcheckbox :presentan una casilla selecionable al usuario, no es autoexcluyente
#setcheckstate : se pude manejar mas valores
#partiallychecked  : -
#checked : visto
#unchecked : vacio
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *
import sys
import os

class MainWindow(QWidget):

    def _init_(self):
        super()._init_()
        layo = QVBoxLayout()


        but2 = QCheckBox("porque", self)

        #se pueden verificar los 3 estados 
        but2.stateChanged.connect(self.show_state)

        #solo se puede verificar dos estados 
        # but2.toggled.connect(self.show_state)

        #se modifica para que quede con 3 estados visto parcial y vacio
        but2.setTristate(True)

        button = QPushButton("verificador", self)
        button.clicked.connect(lambda: self.evaluar_check(but2))

        layo.addWidget(but2)
        layo.addWidget(button)

        self.setLayout(layo)
    

    # para toggled
    # def show_state(self, state):
    #     print("\n----show estado---")
    #     if state == True:
    #         print("me electrocutaste pedrito")
    #     else:
    #         print("me electrocutaste pedritaa")
    
    
    #para statechanged
    def show_state(self, state):
        print("\n----show estado---")
        if state == Qt.CheckState.Checked.value:
            print("me electrocutaste pedrito")
        elif state == Qt.CheckState.Unchecked.value:
            print("me desmarcaste pedrito")
        else:
            print("hola amigue retroescavadora caterpiler")


    def evaluar_check(self, but2):
        print("\n-----info check box------")
        print(f"es tri estado : {but2.isTristate()}")
        print(f"verificado : {but2.isChecked()}")
        print(f"Estado : {but2.checkState()}")
        print("--------------------------------------")
