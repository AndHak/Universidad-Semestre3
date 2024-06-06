import pygame
import numpy as np
import pyaudio
import struct

class AudioProcessor:
    def __init__(self):
        pygame.mixer.init()

    def play_music(self, file_path):
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()

    def stop_music(self):
        pygame.mixer.music.stop()

class Visualizer:
    def __init__(self, audio_processor):
        self.audio_processor = audio_processor
        self.chunk = 1024
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = 1
        self.RATE = 44100

    def start_visualization(self):
        p = pyaudio.PyAudio()
        stream = p.open(format=self.FORMAT,
                        channels=self.CHANNELS,
                        rate=self.RATE,
                        input=True,
                        output=True,
                        frames_per_buffer=self.chunk)

        while True:
            data = stream.read(self.chunk)
            decoded_data = np.array(struct.unpack(f"{self.chunk}h", data))

            # Aplicar ecualización aquí

            # Calcular la FFT
            fft_data = np.fft.fft(decoded_data)
            freqs = np.fft.fftfreq(len(decoded_data), 1 / self.RATE)
            freqs = freqs[:len(freqs) // 2]
            fft_data = np.abs(fft_data[:len(fft_data) // 2]) * 2 / (32768 * len(decoded_data))

            # Visualizar la FFT (puedes usar matplotlib para esto)
            # Aquí puedes crear tu visualizador de frecuencia

        stream.stop_stream()
        stream.close()
        p.terminate()

# Uso
audio_processor = AudioProcessor()
visualizer = Visualizer(audio_processor)
visualizer.start_visualization()
