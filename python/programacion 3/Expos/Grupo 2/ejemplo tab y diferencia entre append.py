
from PySide6.QtWidgets import QApplication, QPlainTextEdit, QWidget, QVBoxLayout

class Ventana(QWidget):
    def __init__(self):
        super().__init__()
        self.ui_diferencia_append_insertPlainText()

    def ui_tab_distance(self):
        # Crear el widget de edición de texto
        self.editor = QPlainTextEdit(self)

        # Cambiar el texto plano
        self.editor.setPlainText("Hola, mundo!")

        # Cambiar la distancia de tabulación
        self.editor.setTabStopDistance(10)

        # Crear un layout vertical y añadir el editor de texto
        layout = QVBoxLayout(self)
        layout.addWidget(self.editor)

        self.setLayout(layout)

    def ui_diferencia_append_insertPlainText(self):
        layout = QVBoxLayout()
        self.editor = QPlainTextEdit()
        self.editor.insertPlainText("¡Hola, ")
        # Ahora el contenido del editor es: "¡Hola, "
        self.editor.insertPlainText("¡Holaaa ")

        # Usamos appendPlainText() para agregar texto al final del contenido existente
        self.editor.appendPlainText("Mundo!")
        # Ahora el contenido del editor es: "¡Hola, Mundo!"
        layout.addWidget(self.editor)

        self.setLayout(layout)


if "__main__" == __name__:
    app = QApplication([])
    window = Ventana()
    window.show()
    app.exec()