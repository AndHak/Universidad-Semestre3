from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from pydub import AudioSegment
import wave
import struct
import numpy as np


# Función para leer el archivo de audio
def obtener_datos_audio(ruta_archivo):
    # Leer el archivo de audio usando pydub
    audio = AudioSegment.from_file(ruta_archivo)
    # Configurar el audio a un canal y ancho de muestra específico
    audio = audio.set_channels(1).set_sample_width(2)
    # Exportar el audio a un archivo WAV temporal
    temp_wav_path = "temp.wav"
    audio.export(temp_wav_path, format="wav")
    # Abrir el archivo WAV temporal y leer los datos de audio
    archivo_wav = wave.open(temp_wav_path, 'rb')
    frames = archivo_wav.readframes(-1)
    archivo_wav.close()
    # Convertir los datos de audio en un arreglo numpy
    datos_audio = np.array(struct.unpack('{n}h'.format(n=len(frames)//2), frames))
    return datos_audio, temp_wav_path

# Clase para el widget del visualizador
class WidgetVisualizador(QWidget):
    def __init__(self, datos_audio, total_frames, tamaño_frame, num_barras, sensibilidad, parent=None):
        super().__init__(parent)
        self.datos_audio = datos_audio
        self.total_frames = total_frames
        self.tamaño_frame = tamaño_frame
        self.num_barras = num_barras
        self.sensibilidad = sensibilidad
        self.frame = 0
        self.paused_frame = 0 
        self.amplitudes_anteriores = [0] * num_barras
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.actualizar_visualizador)
        self.timer.start(50)
        self.espacio_barra = 0.3

    def obtener_amplitud(self):
        inicio = self.frame * self.tamaño_frame
        fin = min(inicio + self.tamaño_frame, len(self.datos_audio))
        segmento = self.datos_audio[inicio:fin]
        ancho_barra = int(self.width() / (self.num_barras * (1 + self.espacio_barra)))
        amplitudes = []
        for i in range(self.num_barras):
            max_amplitud = np.max(np.abs(segmento[i * ancho_barra:(i + 1) * ancho_barra]))
            if max_amplitud > self.sensibilidad:
                amplitudes.append(max_amplitud)
            else:
                amplitudes.append(0)
        return amplitudes

    def actualizar_visualizador(self):
        self.frame += 1
        if self.frame >= self.total_frames:
            self.frame = 0
        self.update()

    def paintEvent(self, event):
        amplitudes = self.obtener_amplitud()
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        self.dibujar_barras(painter, amplitudes)
        
    def dibujar_barras(self, painter, amplitudes):
        ancho_barra = int(self.width() / (self.num_barras * (1 + self.espacio_barra)))
        color = QColor("#9796bd")
        rect = self.rect()
        for i, amplitud in enumerate(amplitudes):
            amplitud_normalizada = amplitud / 32768.0
            amplitud_suavizada = (self.amplitudes_anteriores[i] * 0.5) + (amplitud_normalizada * 0.5)
            altura_barra = int(amplitud_suavizada * self.height())
            painter.setBrush(QBrush(color))
            painter.setPen(Qt.NoPen)
            painter.drawRoundedRect(i * (1 + self.espacio_barra) * ancho_barra + rect.x(),
                                    (rect.height() - altura_barra) // 2,
                                    ancho_barra - 2, altura_barra, 10, 10)
            self.amplitudes_anteriores[i] = amplitud_suavizada

    def detener_visualizador(self):
        self.paused_frame = self.frame  # Guardar la posición del frame al pausar
        self.amplitudes_anteriores = [0] * self.num_barras  # Resetear amplitudes a cero
        self.hide()
        self.update()  # Forzar una actualización de la pantalla con barras en cero

    def reanudar_visualizador(self):
        self.frame = self.paused_frame  # Reanudar desde la posición guardada
        self.update()  # Forzar una actualización de la pantalla con las barras en la posición correcta
        self.show()
        self.timer.start(50)

    def actualizar_frame(self, frame):
        self.frame = frame
        self.show()
        self.update()