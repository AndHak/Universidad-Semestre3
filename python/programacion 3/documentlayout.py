from PySide6.QtWidgets import QApplication, QTextEdit
from PySide6.QtGui import QTextDocument, QFont, QTextCursor

app = QApplication([])

# Crear un QTextEdit
editor = QTextEdit()

# Crear un QTextDocument y establecerlo en el QTextEdit
documento = QTextDocument()
editor.setDocument(documento)

# Agregar texto al documento
documento.setPlainText("Este es un ejemplo de texto en un QTextDocument.")

# Configurar algunas propiedades de formato
cursor = editor.textCursor()
cursor.select(QTextCursor.Document)
formato = cursor.charFormat()
formato.setFont(QFont("Arial", 12))
cursor.setCharFormat(formato)

# Mostrar el QTextEdit
editor.show()

# Ejecutar la aplicación
app.exec_()
