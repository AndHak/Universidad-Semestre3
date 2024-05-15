from PySide6.QtWidgets import QApplication, QPlainTextEdit, QVBoxLayout, QPushButton, QWidget

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui_intermedio()
    
    def ui_sencillo(self):
        layout = QVBoxLayout()
        # Crear un QPlainTextEdit
        self.editor = QPlainTextEdit()

        # Usar setPlainText para establecer el texto del editor
        self.editor.setPlainText("¡Hola, mundo!")


        layout.addWidget(self.editor)
        self.setLayout(layout)
    
    def ui_intermedio(self):

        layout = QVBoxLayout()
        # Crear un QPlainTextEdit
        self.editor = QPlainTextEdit()

        # Usar setPlainText para establecer el texto del editor
        self.editor.setPlainText("¡Hola, mundo!")

        layout.addWidget(self.editor)

        # Crear un botón para imprimir el texto del editor
        button_print = QPushButton("Imprimir texto")
        button_print.clicked.connect(self.print_text)
        layout.addWidget(button_print)

        # Crear un botón para alternar el estado de solo lectura del editor
        button_toggle = QPushButton("Alternar solo lectura")
        button_toggle.clicked.connect(self.toggle_read_only)
        layout.addWidget(button_toggle)

        # Crear un botón para eliminar el texto del editor
        button_clear = QPushButton("Eliminar texto")
        button_clear.clicked.connect(self.clear_text)
        layout.addWidget(button_clear)

        self.setLayout(layout)

    def print_text(self):
        print(self.editor.toPlainText())#imprime el texto actual del editor

    def toggle_read_only(self):
        self.editor.setReadOnly(not self.editor.isReadOnly())

    def clear_text(self):
        self.editor.clear()

if "__main__" == __name__:
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()