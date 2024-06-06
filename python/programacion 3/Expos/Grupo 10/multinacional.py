import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTableWidget, QTableWidgetItem, QTableView, QLineEdit, QLabel, QMessageBox
from PySide6.QtGui import QStandardItemModel, QStandardItem

def crear_campo_entrada(etiqueta, layout):
    label = QLabel(etiqueta.capitalize())
    campo = QLineEdit()
    layout.addWidget(label)
    layout.addWidget(campo)
    return campo

def mostrar_error(mensaje):
    mensaje_error = QMessageBox()
    mensaje_error.setIcon(QMessageBox.Critical)
    mensaje_error.setText(mensaje)
    mensaje_error.setWindowTitle("Error")
    mensaje_error.exec()

def validar_entradas(nombre, edad, pais):
    if not nombre or not edad or not pais:
        mostrar_error("Todos los campos son obligatorios y no deben contener solo espacios en blanco.")
        return False
    if not edad.isdigit():
        mostrar_error("La edad debe ser un número.")
        return False
    if any(char.isdigit() for char in nombre):
        mostrar_error("El nombre no debe contener números.")
        return False
    if any(char.isdigit() for char in pais):
        mostrar_error("El país no debe contener números.")
        return False
    return True

def agregar_estudiante(tabla, modelo, campos):
    nombre = campos["nombre"].text().strip()
    edad = campos["edad"].text().strip()
    pais = campos["pais"].text().strip()

    if validar_entradas(nombre, edad, pais):
        fila_actual = tabla.rowCount()
        tabla.insertRow(fila_actual)
        tabla.setItem(fila_actual, 0, QTableWidgetItem(nombre))
        tabla.setItem(fila_actual, 1, QTableWidgetItem(edad))
        tabla.setItem(fila_actual, 2, QTableWidgetItem(pais))

        modelo.appendRow([QStandardItem(nombre), QStandardItem(edad), QStandardItem(pais)])

        for campo in campos.values():
            campo.clear()

def eliminar_estudiante(tabla, modelo):
    filas_seleccionadas = set(index.row() for index in tabla.selectedIndexes())
    for fila in sorted(filas_seleccionadas, reverse=True):
        tabla.removeRow(fila)
        modelo.removeRow(fila)

class VentanaPrincipal(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Sistema de Gestión de Estudiantes")
        self.setGeometry(100, 100, 800, 600)

        self.layout = QVBoxLayout(self)

        # Campos de entrada de datos
        self.campos = {
            "nombre": crear_campo_entrada("nombre", self.layout),
            "edad": crear_campo_entrada("edad", self.layout),
            "pais": crear_campo_entrada("pais", self.layout)
        }

        # Botones de operación
        self.boton_agregar = QPushButton("Agregar Estudiante")
        self.boton_agregar.clicked.connect(self.on_agregar_estudiante)
        self.layout.addWidget(self.boton_agregar)

        self.boton_eliminar = QPushButton("Eliminar Estudiante")
        self.boton_eliminar.clicked.connect(self.on_eliminar_estudiante)
        self.layout.addWidget(self.boton_eliminar)

        # Tabla de datos
        self.tabla = QTableWidget()
        self.tabla.setColumnCount(3)
        self.tabla.setHorizontalHeaderLabels(["Nombre", "Edad", "País"])
        self.layout.addWidget(self.tabla)

        # Vista de tabla
        self.vista_tabla = QTableView()
        self.layout.addWidget(self.vista_tabla)

        self.setLayout(self.layout)

        # Modelo de datos para la vista de tabla
        self.modelo = QStandardItemModel()
        self.modelo.setHorizontalHeaderLabels(["Nombre", "Edad", "País"])
        self.vista_tabla.setModel(self.modelo)

    def on_agregar_estudiante(self):
        agregar_estudiante(self.tabla, self.modelo, self.campos)

    def on_eliminar_estudiante(self):
        eliminar_estudiante(self.tabla, self.modelo)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec())
