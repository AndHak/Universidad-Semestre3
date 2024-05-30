import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTableWidget, QTableWidgetItem, QTableView, QLineEdit, QLabel
from PySide6.QtGui import QStandardItemModel, QStandardItem

class VentanaPrincipal(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Sistema de Gestión de Estudiantes")
        self.setGeometry(100, 100, 800, 600)

        self.layout = QVBoxLayout(self)

        # Campos de entrada de datos
        self.campos = {
            "nombre": QLineEdit(),
            "edad": QLineEdit(),
            "pais": QLineEdit()
        }

        for etiqueta, campo in self.campos.items():
            self.layout.addWidget(QLabel(etiqueta.capitalize()))
            self.layout.addWidget(campo)

        # Botones de operación
        self.boton_agregar = QPushButton("Agregar Estudiante")
        self.boton_agregar.clicked.connect(self.agregar_estudiante)
        self.layout.addWidget(self.boton_agregar)

        self.boton_eliminar = QPushButton("Eliminar Estudiante")
        self.boton_eliminar.clicked.connect(self.eliminar_estudiante)
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


    def validar_entradas(self, nombre, edad, pais):
        if not nombre or not edad or not pais:
            self.mostrar_error("Todos los campos son obligatorios y no deben contener solo espacios en blanco.")
            return False
        if not edad.isdigit():
            self.mostrar_error("La edad debe ser un número.")
            return False
        if any(char.isdigit() for char in nombre):
            self.mostrar_error("El nombre no debe contener números.")
            return False
        if any(char.isdigit() for char in pais):
            self.mostrar_error("El país no debe contener números.")
            return False
        return True

    def agregar_estudiante(self):
        nombre = self.campos["nombre"].text().strip()
        edad = self.campos["edad"].text().strip()
        pais = self.campos["pais"].text().strip()

        if self.validar_entradas(nombre, edad, pais):
            self.tabla.insertRow(self.tabla.rowCount())
            self.tabla.setItem(self.tabla.rowCount() - 1, 0, QTableWidgetItem(nombre))
            self.tabla.setItem(self.tabla.rowCount() - 1, 1, QTableWidgetItem(edad))
            self.tabla.setItem(self.tabla.rowCount() - 1, 2, QTableWidgetItem(pais))

            self.modelo.appendRow([QStandardItem(nombre), QStandardItem(edad), QStandardItem(pais)])

            for campo in self.campos.values():
                campo.clear()

    def eliminar_estudiante(self):
        filas_seleccionadas = set(index.row() for index in self.tabla.selectedIndexes())
        for fila in sorted(filas_seleccionadas, reverse=True):
            self.tabla.removeRow(fila)
            self.modelo.removeRow(fila)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec())
