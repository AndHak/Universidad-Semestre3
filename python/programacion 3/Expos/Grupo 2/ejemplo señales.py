from PySide6.QtWidgets import QWidget,QPlainTextEdit,QApplication,QVBoxLayout

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Señales")
        layout = QVBoxLayout()
        self.editor = QPlainTextEdit()
        layout.addWidget(self.editor)
        self.setLayout(layout)
        self.editor.setUndoRedoEnabled(False)

        #el cursor de texto tiene un metodo con el que se obtiene el texto seleccionado
        self.editor.selectionChanged.connect(lambda:print(self.editor.textCursor().selectedText()))
        self.editor.textChanged.connect(lambda:print("se cambio el texto"))

if "__main__" == __name__:
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()