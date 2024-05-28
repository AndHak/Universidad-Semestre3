from PySide6.QtWidgets import QWidget,QVBoxLayout,QLabel,QPushButton,QFontDialog,QApplication
from PySide6.QtCore import Qt

class fuentes (QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Seleccionar fuente")
        
        layout_principal = QVBoxLayout()
        label_ejemplo = QLabel("EJemplo de uso de un QFontDialog")
        label_ejemplo.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.label_cambio = QLabel("Texto para cambiar")
        boton_cambiar = QPushButton("Cambiar Fuente") 
        boton_cambiar.clicked.connect(self.abrir_fuentes)          

        layout_principal.addWidget(label_ejemplo)
        layout_principal.addSpacing(20)
        layout_principal.addWidget(self.label_cambio)
        layout_principal.addSpacing(20)
        layout_principal.addWidget(boton_cambiar)

        self.setLayout(layout_principal) 

    def abrir_fuentes(self):
        ok, self.fuente = QFontDialog.getFont()
        if ok:
            self.label_cambio.setFont(self.fuente)


if __name__ == "__main__":
    app = QApplication([])
    ventana = fuentes()
    ventana.show()
    app.exec()        