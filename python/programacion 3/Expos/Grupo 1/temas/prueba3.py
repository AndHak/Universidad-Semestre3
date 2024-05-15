import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QStyleFactory

def main():
    app = QApplication(sys.argv)

    app.setStyle("Macintosh")  # Se establece el tema Macintosh

    window = QMainWindow()
    window.setWindowTitle("Interfaz con Tema Macintosh")

    central_widget = QWidget()
    window.setCentralWidget(central_widget)

    layout = QVBoxLayout()
    central_widget.setLayout(layout)

    boton1 = QPushButton("Botón A", central_widget)
    boton2 = QPushButton("Botón B", central_widget)

    layout.addWidget(boton1)
    layout.addWidget(boton2)
    
    estilos_disponibles = QStyleFactory.keys()
    print("Estilos disponibles:", estilos_disponibles)

    window.show()
    sys.exit(app.exec())

    
if __name__ == "__main__":
    main()
    