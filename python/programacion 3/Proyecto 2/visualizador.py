import sys
import numpy as np
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QPainter, QColor, QBrush, QPen
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget
from pydub import AudioSegment  # Importar la biblioteca para manipulación de audio
import wave
import struct
import os
import pygame  # Importar Pygame para reproducir el audio

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
        # Configuración inicial del widget
        self.datos_audio = datos_audio  # Almacena los datos de audio
        self.total_frames = total_frames  # Almacena el número total de fotogramas de audio
        self.tamaño_frame = tamaño_frame  # Tamaño de cada fotograma
        self.num_barras = num_barras  # Número de barras en el visualizador
        self.sensibilidad = sensibilidad  # Sensibilidad del visualizador
        self.frame = 0  # Inicializa el fotograma actual
        self.amplitudes_anteriores = [0] * num_barras  # Almacena las amplitudes anteriores para suavizar la visualización
        # Configurar un temporizador para actualizar el visualizador
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.actualizar_visualizador)
        self.timer.start(30)  # Frecuencia de actualización del visualizador (ajustar según la preferencia del usuario)
        # Espacio entre las barras como un porcentaje del ancho total
        self.espacio_barra = 0.3
        
    def obtener_amplitud(self):
        inicio = self.frame * self.tamaño_frame
        fin = inicio + self.tamaño_frame
        if fin >= len(self.datos_audio):
            fin = len(self.datos_audio) - 1
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
        for i, amplitud in enumerate(amplitudes):
            amplitud_normalizada = amplitud / 32768.0
            amplitud_suavizada = (self.amplitudes_anteriores[i] * 0.6) + (amplitud_normalizada * 0.4)
            altura_barra = int(amplitud_suavizada * self.height())
            painter.setBrush(QBrush(color))
            painter.setPen(QPen(color, 1, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
            rect = self.rect()
            painter.drawRoundedRect(i * (1 + self.espacio_barra) * ancho_barra + rect.x(), (rect.height() - altura_barra) // 2,
                                    ancho_barra - 2, altura_barra, 10, 10)
            self.amplitudes_anteriores[i] = amplitud_suavizada
