import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtPrintSupport import *
from PySide6.QtGui import *

class GestorDeTareasApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Gestor de Tareas")
        self.setGeometry(300, 300, 400, 600)

        self.tareas = {}

        self.configurarUI()

    def configurarUI(self):
        self.widgetCentral = QWidget(self)
        self.setCentralWidget(self.widgetCentral)

        self.layout = QVBoxLayout(self.widgetCentral)

        self.listaTareas = QListWidget()
        self.listaTareas.itemChanged.connect(self.manejarCambioItem)
        self.layout.addWidget(self.listaTareas)

        self.botonAgregar = QPushButton("Agregar Tarea")
        self.botonAgregar.clicked.connect(self.agregarTarea)
        self.layout.addWidget(self.botonAgregar)

        self.botonCompletar = QPushButton("Marcar como Completada")
        self.botonCompletar.clicked.connect(self.marcarComoCompletada)
        self.layout.addWidget(self.botonCompletar)

        self.botonEliminar = QPushButton("Eliminar Tarea")
        self.botonEliminar.clicked.connect(self.eliminarTarea)
        self.layout.addWidget(self.botonEliminar)

        self.botonGuardar = QPushButton("Guardar Lista")
        self.botonGuardar.clicked.connect(self.guardarListaTareas)
        self.layout.addWidget(self.botonGuardar)

        self.botonCargar = QPushButton("Cargar Lista")
        self.botonCargar.clicked.connect(self.cargarListaTareas)
        self.layout.addWidget(self.botonCargar)

        self.etiquetaEstado = QLabel("")
        self.layout.addWidget(self.etiquetaEstado)

    def agregarTarea(self):
        tarea, ok = QInputDialog.getText(self, "Agregar Tarea", "Ingrese la tarea:")
        tarea = tarea.strip()  
        if ok and tarea:
            self.tareas[tarea] = False
            item = QListWidgetItem(tarea)
            item.setFlags(item.flags() | Qt.ItemIsUserCheckable)
            item.setCheckState(Qt.Unchecked)
            self.listaTareas.addItem(item)
            self.etiquetaEstado.setText(f"'{tarea}' agregada.")
        else:
            self.etiquetaEstado.setText("No se agregó ninguna tarea.")


    def manejarCambioItem(self, item):
        tarea = item.text()
        completada = item.checkState() == Qt.Checked
        self.tareas[tarea] = completada
        estado = "completada" if completada else "pendiente"
        self.etiquetaEstado.setText(f"Tarea '{tarea}' marcada como {estado}.")



    def marcarComoCompletada(self):
        itemActual = self.listaTareas.currentItem()
        if itemActual:
            tarea = itemActual.text()
            respuesta = QMessageBox.question(self, "Confirmar", f"Marcar '{tarea}' como hecha?", QMessageBox.Yes | QMessageBox.No)
            if respuesta == QMessageBox.Yes:
                itemActual.setCheckState(Qt.Checked)
                self.etiquetaEstado.setText(f"'{tarea}' completada.")
            else:
                self.etiquetaEstado.setText("Acción cancelada.")

    def eliminarTarea(self):
        itemActual = self.listaTareas.currentItem()
        if itemActual:
            tarea = itemActual.text()
            respuesta = QMessageBox.question(self, "Confirmar", f"¿Eliminar '{tarea}'?", QMessageBox.Yes | QMessageBox.No)
            if respuesta == QMessageBox.Yes:
                self.tareas.pop(tarea)
                self.listaTareas.takeItem(self.listaTareas.row(itemActual))
                self.etiquetaEstado.setText(f"'{tarea}' eliminada.")
            else:
                self.etiquetaEstado.setText("Accion cancelada")

    def guardarListaTareas(self):
        if not self.tareas:
            QMessageBox.warning(self, "Advertencia", "Agregue una tarea")
            return
        
        nombreArchivo, _ = QFileDialog.getSaveFileName(self, "Guardar Lista", "", "Archivos de texto (*.txt)")
        if nombreArchivo:
            try:
                with open(nombreArchivo, 'w') as archivo:
                    for tarea, completada in self.tareas.items():
                        archivo.write(f"{tarea},{completada}\n")
                self.etiquetaEstado.setText("Lista guardada.")
            except Exception as e:
                dialogoError = QErrorMessage(self)
                dialogoError.showMessage(f"No se pudo guardar: {e}")


    def cargarListaTareas(self):
        nombreArchivo, _ = QFileDialog.getOpenFileName(self, "Cargar Lista", "", "Archivos de Texto (*.txt)")
        if nombreArchivo:
            try:
                with open(nombreArchivo, 'r') as archivo:
                    lineas = archivo.readlines()
                    if self.tareas:
                        respuesta = QMessageBox.question(self, "Confirmar", "Borrar lista actual?", QMessageBox.Yes | QMessageBox.No)
                        if respuesta == QMessageBox.Yes:
                            self.tareas.clear()
                            self.listaTareas.clear()
                        else:
                            return
                    for linea in lineas:
                        tarea, completada = linea.strip().split(',')
                        self.tareas[tarea] = completada == 'True'
                        item = QListWidgetItem(tarea)
                        item.setFlags(item.flags() | Qt.ItemIsUserCheckable)
                        item.setCheckState(Qt.Checked if completada == 'True' else Qt.Unchecked)
                        self.listaTareas.addItem(item)
                self.etiquetaEstado.setText("Lista cargada.")
            except Exception as e:
                dialogoError = QErrorMessage(self)
                dialogoError.showMessage(f"No se pudo cargar: {e}")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = GestorDeTareasApp()
    ventana.show()
    sys.exit(app.exec())
