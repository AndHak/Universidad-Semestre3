from PySide6.QtWidgets import QWidget,QPlainTextEdit,QApplication,QVBoxLayout, QPlainTextDocumentLayout

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.cursor_width()

    def cursor_width(self):
        layout = QVBoxLayout()
        self.editor = QPlainTextEdit()

        #Creamos el QPLainTextDocumentLayout y le pasamos como parametro el documento del editor

        text_document_layout = QPlainTextDocumentLayout(self.editor.document())
        self.editor.document().setDocumentLayout(text_document_layout)
        print(text_document_layout.cursorWidth())
        text_document_layout.setCursorWidth(30)

        layout.addWidget(self.editor)
        self.setLayout(layout)

if "__main__" == __name__:
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()