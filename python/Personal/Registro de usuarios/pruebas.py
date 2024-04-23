from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QLabel, QWidget, QApplication
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt

class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mi Ventana")
        self.resize(800, 600)  # Tamaño inicial de la ventana

        self.root_layout = QVBoxLayout()
        self.root_widget = QWidget()
        self.root_widget.setLayout(self.root_layout)
        self.setCentralWidget(self.root_widget)

        self.pagina_mapa_mundi()

    def pagina_mapa_mundi(self):
        self.label_backgraund = QLabel()
        self.label_backgraund.setAlignment(Qt.AlignCenter)
        self.root_layout.addWidget(self.label_backgraund)

        self.imagen_mapa_mundi = QPixmap("images_dashboard/map_map_map.jpg")
        self.label_backgraund.setPixmap(self.imagen_mapa_mundi.scaled(self.label_backgraund.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.label_backgraund.setPixmap(self.imagen_mapa_mundi.scaled(self.label_backgraund.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    ventana = MiVentana()
    ventana.show()
    sys.exit(app.exec_())
