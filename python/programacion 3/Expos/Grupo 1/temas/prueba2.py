import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget

def main():
    app = QApplication(sys.argv)

    app.setStyle("Windows")  # Se establece el tema Windows

    window = QMainWindow()
    window.setWindowTitle("Interfaz con Tema Windows")

    central_widget = QWidget()
    window.setCentralWidget(central_widget)

    layout = QVBoxLayout()
    central_widget.setLayout(layout)

    boton1 = QPushButton("Botón 1", central_widget)
    boton2 = QPushButton("Botón 2", central_widget)
    layout.addWidget(boton1)
    layout.addWidget(boton2)

    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
