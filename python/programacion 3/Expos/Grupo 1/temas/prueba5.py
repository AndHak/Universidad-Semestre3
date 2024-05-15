import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from PySide6.QtGui import QColor, Qt, QPalette

def main():
    app = QApplication(sys.argv)

    app.setStyle("Fusion")
    app.setPalette(QApplication.style())

    dark_palette = app.palette()
    dark_palette.setColor(QPalette.Window, QColor("Black"))
    dark_palette.setColor(QPalette.WindowText, Qt.white)

    app.setPalette(dark_palette)

    window = QMainWindow()
    window.setWindowTitle("Interfaz con Tema Oscuro")

    boton1 = QPushButton("Botón1", window)
    boton1.setGeometry(50, 50, 50, 30)

    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
