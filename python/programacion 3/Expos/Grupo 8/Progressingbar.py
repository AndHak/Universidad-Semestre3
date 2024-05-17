import sys
import os
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QHBoxLayout, QVBoxLayout, QWidget, QFrame, QLabel, QSlider
from PySide6.QtCore import Qt, QPoint, QSize
from PySide6.QtGui import QIcon, QPixmap
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, APIC

class CustomTitleBar(QWidget):
    basedir = os.path.dirname(__file__)
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedHeight(40)
        self.parent = parent

        # Crear botones de la barra de título
        self.closeButton = QPushButton()
        self.closeButton.setFixedSize(QSize(50,40))
        self.minimizeButton = QPushButton()
        self.minimizeButton.setFixedSize(QSize(40,40))
        self.maximizeButton = QPushButton()
        self.maximizeButton.setFixedSize(QSize(40,40))

        # Configurar botones para usar íconos personalizados
        self.closeButton.setIcon(QIcon(os.path.join(self.basedir, "img/cerrar.png")))
        self.minimizeButton.setIcon(QIcon(os.path.join(self.basedir, "img/minimizar.png")))
        self.maximizeButton.setIcon(QIcon(os.path.join(self.basedir, "img/maximizar.png")))

        # Estilo de los botones
        self.closeButton.setStyleSheet(self.getCloseButtonStyle())
        self.minimizeButton.setStyleSheet(self.getButtonStyle())
        self.maximizeButton.setStyleSheet(self.getButtonStyle())

        # Conectar los botones a sus funciones
        self.closeButton.clicked.connect(self.closeWindow)
        self.minimizeButton.clicked.connect(self.minimizeWindow)
        self.maximizeButton.clicked.connect(self.maximizeWindow)

        # Diseño de los botones
        layout = QHBoxLayout()
        layout.addStretch()
        layout.addWidget(self.minimizeButton)
        layout.addWidget(self.maximizeButton)
        layout.addWidget(self.closeButton)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        self.setLayout(layout)

        # Estilo de la barra de título
        self.setStyleSheet("""
            background-color: #000000;
        """)

    def getButtonStyle(self):
        return """
        QPushButton {
            background-color: transparent;
            border: none;
        }
        QPushButton:hover {
            background-color: #3e3e3e;
        }
        """

    def getCloseButtonStyle(self):
        return """
        QPushButton {
            background-color: transparent;
            border: none;
        }
        QPushButton:hover {
            background-color: #ff4c4c;
        }
        """

    def closeWindow(self):
        self.parent.close()

    def minimizeWindow(self):
        self.parent.showMinimized()

    def maximizeWindow(self):
        if self.parent.isMaximized():
            self.parent.showNormal()
        else:
            self.parent.showMaximized()

    def mousePressEvent(self, event):
        self.oldPos = event.globalPosition().toPoint()

    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPosition().toPoint() - self.oldPos)
        self.parent.move(self.parent.x() + delta.x(), self.parent.y() + delta.y())
        self.oldPos = event.globalPosition().toPoint()

class MainWindow(QMainWindow):
    basedir = os.path.dirname(__file__)
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setGeometry(100, 100, 400, 600)

        self.titleBar = CustomTitleBar(self)
        self.setWindowTitle("Music Player")

        self.root_layout = QVBoxLayout()
        self.root_layout.setContentsMargins(0,0,0,0)

        self.frame_barra = QFrame()
        self.frame_app_reproductor = QFrame()

        self.root_layout.addWidget(self.frame_barra, 1)
        self.root_layout.addWidget(self.frame_app_reproductor, 99) 

        layout = QVBoxLayout()
        layout.addWidget(self.titleBar)
        layout.addStretch()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        self.frame_barra.setLayout(layout)
        self.frame_barra.setStyleSheet("background-color: #0d0d0d")

        container = QWidget()
        container.setLayout(self.root_layout)
        self.setCentralWidget(container)

        self.desarrollo_reproductor()

        # Estilo oscuro para la ventana
        self.setStyleSheet("""
            QMainWindow {
                background-color: #121212;
            }
        """)

    def desarrollo_reproductor(self):
        self.root_reproductor = QVBoxLayout()
        self.root_reproductor.setContentsMargins(20, 20, 20, 20)
        self.root_reproductor.setSpacing(20)

        self.frame_imagen_song = QFrame()
        self.frame_info_song = QFrame()
        self.frame_barra_progreso = QFrame()
        self.frame_botones_rep = QFrame()

        # Desarrollo del primer frame (imagen de la canción)
        self.layout_imagen_song = QVBoxLayout()
        self.label_imagen = QLabel()
        self.layout_imagen_song.addWidget(self.label_imagen)
        self.frame_imagen_song.setLayout(self.layout_imagen_song)

        # Desarrollo del segundo frame (información de la canción)
        self.layout_info_song = QVBoxLayout()
        self.label_titulo = QLabel("Titulo:")
        self.label_artista = QLabel("Artista: ")
        self.label_titulo.setStyleSheet("color: white; font-size: 18px;")
        self.label_artista.setStyleSheet("color: gray; font-size: 14px;")
        self.layout_info_song.addWidget(self.label_titulo)
        self.layout_info_song.addWidget(self.label_artista)
        self.frame_info_song.setLayout(self.layout_info_song)

        # Desarrollo del tercer frame (barra de progreso)
        self.layout_barra_progreso = QHBoxLayout()
        self.layout_barra_progreso.setSpacing(15)
        self.label_tiempo_transcurrido = QLabel("00:00")
        self.label_tiempo_transcurrido.setStyleSheet("color: white; font-size: 13px;")
        self.slider_progreso = QSlider(Qt.Horizontal)
        self.slider_progreso.setStyleSheet("""
            QSlider::groove:horizontal {
                background-color: white;
                height: 6px;
                border-radius: 3px;
            }
            QSlider::handle:horizontal {
                background-color: white;
                width: 12px;
                height: 12px;
                border-radius: 6px;
                margin: -3px 0;
            }
            QSlider::add-page:horizontal {
                background-color: gray;
            }
        """)
        self.label_tiempo_total = QLabel("00:00")
        self.label_tiempo_total.setStyleSheet("color: white; font-size: 13px;")

        self.layout_barra_progreso.addWidget(self.label_tiempo_transcurrido)
        self.layout_barra_progreso.addWidget(self.slider_progreso)
        self.layout_barra_progreso.addWidget(self.label_tiempo_total)

        self.frame_barra_progreso.setLayout(self.layout_barra_progreso)

        # Desarrollo del cuarto frame (botones de reproducción)
        self.layout_botones_rep = QHBoxLayout()
        self.layout_botones_rep.setContentsMargins(0,0,0,20)
        self.layout_botones_rep.setSpacing(20)
        self.layout_botones_rep.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.boton_retroceder = QPushButton()
        self.boton_retroceder.setContentsMargins(0,0,0,0)
        self.boton_retroceder.setIconSize(QSize(38,38))
        self.boton_retroceder.setIcon(QIcon(os.path.join(self.basedir, "img/back.png")))
        # Botón de pausa
        self.boton_play = QPushButton()
        self.boton_play.setIconSize(QSize(86, 86))
        self.boton_play.setContentsMargins(0,0,0,0)
        self.boton_play.setIcon(QIcon(os.path.join(self.basedir, "img/pausa.png")))

        self.boton_avanzar = QPushButton()
        self.boton_avanzar.setIconSize(QSize(38,38))
        self.boton_avanzar.setContentsMargins(0,0,0,0)
        self.boton_avanzar.setIcon(QIcon(os.path.join(self.basedir, "img/next.png")))
        self.boton_retroceder.setStyleSheet("background-color: transparent; border: none;")
        self.boton_play.setStyleSheet("background-color: transparent; border: none;")
        self.boton_avanzar.setStyleSheet("background-color: transparent; border: none;")

        self.boton_retroceder.setCursor(Qt.PointingHandCursor)
        self.boton_play.setCursor(Qt.PointingHandCursor)
        self.boton_avanzar.setCursor(Qt.PointingHandCursor)


        self.layout_botones_rep.addWidget(self.boton_retroceder)
        self.layout_botones_rep.addWidget(self.boton_play)
        self.layout_botones_rep.addWidget(self.boton_avanzar)
        self.frame_botones_rep.setLayout(self.layout_botones_rep)

        self.root_reproductor.addWidget(self.frame_imagen_song)
        self.root_reproductor.addWidget(self.frame_info_song)
        self.root_reproductor.addWidget(self.frame_barra_progreso)
        self.root_reproductor.addWidget(self.frame_botones_rep)

        self.frame_app_reproductor.setLayout(self.root_reproductor)



        def mousePressEvent(self, event):
            self.oldPos = event.globalPosition().toPoint()

        def mouseMoveEvent(self, event):
            delta = QPoint(event.globalPosition().toPoint() - self.oldPos)
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.oldPos = event.globalPosition().toPoint()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
