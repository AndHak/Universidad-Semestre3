import sys
import vlc
import time
from PySide6.QtCore import Qt, QTimer
from PySide6.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget, QScrollArea, QFrame

class LyricsWidget(QWidget):
    def __init__(self, lyrics, audio_file):
        super().__init__()

        self.lyrics = lyrics
        self.current_line = 0

        self.layout = QVBoxLayout()
        self.layout.setSpacing(20)  # Espaciado entre las líneas
        self.labels = []

        for line in lyrics:
            label = QLabel(line)
            label.setAlignment(Qt.AlignCenter)
            label.setStyleSheet("font-size: 20px;")
            self.layout.addWidget(label)
            self.labels.append(label)

        self.container = QWidget()
        self.container.setLayout(self.layout)

        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setWidget(self.container)
        self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.scroll_area)

        # Un QLabel para la línea actual fija en el centro
        self.current_label = QLabel()
        self.current_label.setAlignment(Qt.AlignCenter)
        self.current_label.setStyleSheet("font-size: 20px; font-weight: bold;")
        self.current_label.setFrameStyle(QFrame.Box | QFrame.Plain)
        self.current_label.setLineWidth(2)

        # Añadir la etiqueta actual fija a un contenedor con diseño
        container_layout = QVBoxLayout()
        container_layout.addLayout(main_layout)
        container_layout.addWidget(self.current_label, alignment=Qt.AlignCenter)

        self.setLayout(container_layout)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_current_line)
        self.timer.start(2000)  # Cambia el tiempo según la velocidad de la canción

        # Reproductor de audio
        self.player = vlc.MediaPlayer(audio_file)
        self.player.play()

    def update_current_line(self):
        if self.current_line > 0:
            self.labels[self.current_line - 1].setStyleSheet("font-size: 20px;")  # Resetea la línea anterior
        if self.current_line < len(self.labels):
            self.current_label.setText(self.labels[self.current_line].text())
            self.labels[self.current_line].setStyleSheet("font-size: 20px;")
            
            # Desplazar la vista hacia arriba
            scroll_value = self.scroll_area.verticalScrollBar().value() + self.labels[self.current_line].height() + self.layout.spacing()
            self.scroll_area.verticalScrollBar().setValue(scroll_value)

            self.current_line += 1

class MainWindow(QWidget):
    def __init__(self, lyrics, audio_file):
        super().__init__()
        self.lyrics_widget = LyricsWidget(lyrics, audio_file)
        layout = QVBoxLayout()
        layout.addWidget(self.lyrics_widget)
        self.setLayout(layout)

if __name__ == "__main__":
    lyrics = [
        "Línea 1 de la canción",
        "Línea 2 de la canción",
        "Línea 3 de la canción",
        "Línea 4 de la canción",
        "Línea 5 de la canción",
        "Línea 6 de la canción",
        # Agrega más líneas según sea necesario
    ]
    
    audio_file = "python\programacion 3\Proyecto 2\songs\Shape of my Heart (Lyrics) [Sting](MP3_160K).mp3" 
    
    app = QApplication(sys.argv)
    window = MainWindow(lyrics, audio_file)
    window.setGeometry(100, 100, 600, 400)
    window.show()
    sys.exit(app.exec())
