from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import time


class CargarArchivosThread(QThread):
    progreso = Signal(int)
    archivos_cargados = Signal(list)

    def __init__(self, archivos):
        super().__init__()
        self.archivos = archivos

    def run(self):
        archivos_cargados = []
        total_archivos = len(self.archivos)
        print("Total de archivos:", total_archivos)
        for i, archivo in enumerate(self.archivos):
            archivos_cargados.append(archivo)
            progreso = int((i + 1) / total_archivos * 100)
            print("Progreso:", progreso)
            self.progreso.emit(progreso)
            time.sleep(1)  # Simulate processing time (remove this in actual implementation)
        self.archivos_cargados.emit(archivos_cargados)