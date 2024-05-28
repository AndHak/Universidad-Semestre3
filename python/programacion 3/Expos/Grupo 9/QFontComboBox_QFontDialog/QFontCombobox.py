from PySide6.QtWidgets import QWidget,QVBoxLayout,QLabel,QFontComboBox,QHBoxLayout,QPushButton,QApplication

class ventana(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QComboBox")
        self.muestra_1()

    # cambio de fuente directo 
    def muestra_1(self):
        layout_principal = QVBoxLayout()

        self.label_cambio = QLabel("Texto a cambiar")
        
        self.fuente_combo = QFontComboBox()
        self.fuente_combo.currentFontChanged.connect(self.cambiar_fuente_1)

        layout_principal.addWidget(self.label_cambio)
        layout_principal.addWidget(self.fuente_combo)

        self.setLayout(layout_principal)

    def cambiar_fuente_1(self,fuente):
        self.label_cambio.setFont(fuente)   

    # cambio de fuente con boton
    def muestra_2(self):
        layout_principal = QHBoxLayout()

        layout_der = QVBoxLayout() 
        self.label_cambiar = QLabel("Este label sera cambiado")
        self.boton_cambiar = QPushButton("Cambiar Fuente")
        self.boton_cambiar.clicked.connect(self.aplicar_cambio)
        
        self.combo = QFontComboBox()
        self.combo.currentFontChanged.connect(self.cambiar_fuente_2)

        layout_der.addWidget(self.label_cambiar)
        layout_der.addWidget(self.boton_cambiar)
        
        layout_principal.addWidget(self.combo)
        layout_principal.addLayout(layout_der)

        self.setLayout(layout_principal)

    def cambiar_fuente_2(self,fuente):
        self.nueva_fuente = fuente    

    def aplicar_cambio(self):
        self.label_cambiar.setFont(self.nueva_fuente)    


if __name__ == "__main__":
    app = QApplication([])
    window = ventana()
    window.show()
    app.exec()