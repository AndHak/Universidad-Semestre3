from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QPushButton, QFrame

class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ejemplo de Barra de Navegación")

        # Layout principal para toda la ventana
        self.root_layout = QVBoxLayout()

        # Crear la barra de navegación y agregar botones
        self.barra_de_navegacion()

        # Crear otros widgets y agregarlos al layout principal
        self.widget1 = QPushButton("Widget 1")
        self.root_layout.addWidget(self.widget1)

        self.widget2 = QPushButton("Widget 2")
        self.root_layout.addWidget(self.widget2)

        # Crear un frame principal
        self.frame_principal = QFrame()
        self.root_layout.addWidget(self.frame_principal)

        # Establecer el layout principal en la ventana
        self.main_widget = QWidget()
        self.main_widget.setLayout(self.root_layout)
        self.setCentralWidget(self.main_widget)

    def barra_de_navegacion(self):
        # Crear el layout horizontal para la barra de navegación
        self.bar_layout = QHBoxLayout()

        # Crear los botones de la barra de navegación
        self.home_button = QPushButton("HOME")
        self.bar_layout.addWidget(self.home_button)

        self.otro_button = QPushButton("Otro Botón")
        self.bar_layout.addWidget(self.otro_button)

        # Agregar el layout horizontal al layout principal en la parte superior
        self.root_layout.addLayout(self.bar_layout)

if __name__ == "__main__":
    app = QApplication([])
    ventana = MiVentana()
    ventana.show()
    app.exec()
