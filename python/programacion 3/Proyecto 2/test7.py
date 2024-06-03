import sys
from PySide6.QtWidgets import QApplication, QLabel

# Crear una instancia de QApplication
app = QApplication(sys.argv)

# Obtener el nombre del estilo actual
estilo_actual = app.style().objectName()

# Mostrar el estilo actual
print(f"El estilo actual es: {estilo_actual}")

# Crear una ventana simple para mostrar el resultado
ventana = QLabel(f"El estilo actual es: {estilo_actual}")
ventana.resize(300, 100)
ventana.show()

# Ejecutar la aplicación
sys.exit(app.exec())