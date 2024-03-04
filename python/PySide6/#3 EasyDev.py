from PySide6.QtWidgets import *
import sys

class PrimeraVentana(QMainWindow):
    colores = {
        "gris_suave": (213,211,221),
        "beige": (239,208,199)
    }
    def setupUi(self):
        self.setFixedSize(800, 800)

        self.cuadro1 = QFrame(self)
        self.cuadro1.setGeometry(20, 20, 760, 100)
        self.cuadro1.setStyleSheet(f"background-color: rgb{self.colores['gris_suave']};")

        self.cuadro_principal = QFrame(self)
        self.cuadro_principal.setGeometry(20, 140, 500, 640)
        self.cuadro_principal.setStyleSheet(f"background-color: rgb{self.colores['beige']}")

        self.cuadro_info = QFrame(self)
        self.cuadro_info.setGeometry(540, 140, 240, 640)
        self.cuadro_info.setStyleSheet(f"background-color: rgb{self.colores['gris_suave']}")

app = QApplication(sys.argv)

window = PrimeraVentana()
window.setupUi()
window.show()

sys.exit(app.exec_())