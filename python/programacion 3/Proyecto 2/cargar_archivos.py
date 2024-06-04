from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class CargarArchivosThread(QThread):
    progreso = Signal(int)
    archivos_cargados = Signal(list)

    def __init__(self, archivos):
        super().__init__()
        self.archivos = archivos

    def run(self):
        archivos_cargados = []
        total_archivos = len(self.archivos)
        for i, archivo in enumerate(self.archivos):
            archivos_cargados.append(archivo)
            progreso = int((i + 1) / total_archivos * 100)
            self.progreso.emit(progreso)
        self.archivos_cargados.emit(archivos_cargados)