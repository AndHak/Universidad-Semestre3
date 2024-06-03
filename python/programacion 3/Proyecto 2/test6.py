import time
import pygame
from PySide6.QtWidgets import QApplication, QVBoxLayout, QLabel, QWidget
from PySide6.QtCore import QTimer

def leer_archivo_lrc(nombre_archivo):
    with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
        lineas = archivo.readlines()
    
    letras = []
    tiempos = []
    for linea in lineas:
        partes = linea.strip().split(']')
        if len(partes) == 2:
            tiempo = partes[0][1:].strip()  # Elimina el corchete inicial y espacios
            letra = partes[1].strip()
            letras.append(letra)
            tiempos.append(tiempo)
    
    return letras, tiempos

class LetrasVentana(QWidget):
    def __init__(self, letras, tiempos):
        super().__init__()
        self.setWindowTitle("Letras de la Canción")
        self.setGeometry(100, 100, 400, 300)

        self.layout = QVBoxLayout()
        self.letra_label = QLabel()
        self.layout.addWidget(self.letra_label)
        self.setLayout(self.layout)

        self.letras = letras
        self.tiempos = tiempos
        self.indice_letra_actual = 0

        self.tiempo_inicio = time.time()
        self.actualizar_letra()

    def actualizar_letra(self):
        if self.indice_letra_actual < len(self.letras):
            letra = self.letras[self.indice_letra_actual]
            self.letra_label.setText(letra)

            if self.indice_letra_actual + 1 < len(self.tiempos):
                tiempo_actual = time.time() - self.tiempo_inicio
                tiempo_siguiente_letra = self.convertir_a_segundos(self.tiempos[self.indice_letra_actual + 1])
                tiempo_espera = max(0, tiempo_siguiente_letra - tiempo_actual)
                QTimer.singleShot(int(tiempo_espera * 1000), self.actualizar_letra)

            self.indice_letra_actual += 1
        else:
            self.letra_label.setText("Fin de la canción")

    @staticmethod
    def convertir_a_segundos(tiempo):
        minutos, segundos = tiempo.split(':')
        return int(minutos) * 60 + float(segundos)

def main():
    archivo_lrc = 'python/programacion 3/Proyecto 2/Lrc/Sting-Shape-of-my-Heart.lrc'  # Ruta del archivo LRC
    letras, tiempos = leer_archivo_lrc(archivo_lrc)

    # Inicializar pygame y reproducir la canción
    pygame.init()
    cancion = 'python\programacion 3\Proyecto 2\songs\Shape of my Heart (Lyrics) [Sting](MP3_160K).mp3'  # Ruta de la canción
    pygame.mixer.music.load(cancion)
    pygame.mixer.music.play()

    app = QApplication([])
    ventana_letras = LetrasVentana(letras, tiempos)
    ventana_letras.show()
    app.exec()

    pygame.mixer.music.stop()

if __name__ == "__main__":
    main()
