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

