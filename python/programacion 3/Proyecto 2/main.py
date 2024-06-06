from reproductor_de_musica_ui_ui import Ui_MainWindow
from ventana_nombre_ui import Ui_Dialog_nombre
from cargar_archivos import CargarArchivosThread
from visualizador import VisualizerCanvas
from funciones_de_metadatos import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import sys
import os
import webbrowser
import pygame
import random
import pyqtgraph as pg
import numpy as np



class MainMusicApp(QMainWindow, Ui_MainWindow):
    basedir = os.path.dirname(__file__)
    modo_oscuro_activado = False
    paso_agregar_foto = False
    paso_agregar_nombre = False
    paso_agregar_canciones = False
    paso_agregar_favoritas = False
    pasos_totales = 4
    pasos_completados = 0
    def __init__(self):
        super().__init__()
        self.setupUi(self)


        self.setWindowTitle("Pu♩se Music")
        self.setWindowIcon(QIcon(os.path.join(self.basedir, "icons/icons8-music-100.png")))



        self.FPS = 60
        self.RELOG = pygame.time.Clock()
        self.RELOG.tick(self.FPS)

        # Diccionario para almacenar letras con sus marcas de tiempo
        self.letras_con_tiempos = {}

        # Actualizar la letra de la canción cada segundo
        self.timer_letra = QTimer(self)
        self.timer_letra.timeout.connect(self.actualizar_letra)
        self.timer_letra.start(100)  # Actualizar cada segundo
        

        #Carga de canciones
        self.lista_reproducidas = []  # Lista de canciones reproducidas
        self.indice_actual = 0
        self.paused = False
        self.modo_reproduccion = "secuencial"
        self.estado_favoritos = {}

        self.lista_de_reproduccion = [
        os.path.join(self.basedir, "canciones/Cual es esa, Feid Pirlo.mp3"),
        os.path.join(self.basedir, "canciones/Ey Chory, Feid.mp3"),
        os.path.join(self.basedir, "canciones/Mionca, Maluma Pirlo.mp3"),
        os.path.join(self.basedir, "canciones/LUNA, Feid.mp3"),
        os.path.join(self.basedir, "canciones/Nadie Como Tu, Wisin & Yandel.mp3"),
        os.path.join(self.basedir, "canciones/Normal, Feid.mp3"),
        os.path.join(self.basedir, "canciones/Ojitos Chiquitos, Don Omar.mp3"),
        os.path.join(self.basedir, "canciones/Pa que la pases bien, Arcangel.mp3"),
        os.path.join(self.basedir, "canciones/Remix Exclusivo, Feid.mp3"),
        os.path.join(self.basedir, "canciones/Cinco Noches_ Paquito Guzman (letra)(MP3_128K).mp3"),
        os.path.join(self.basedir, "canciones/MI TRISTEZA  -  LUIS ALBERTO POSADA (VIDEO OFICIAL)(MP3_128K).mp3"),
        os.path.join(self.basedir, "canciones/Si sabe Ferxxo, Blessd Feid.mp3"),
        ]

        #Conectar botones stacked
        self.settings_button.clicked.connect(self.mostrar_pagina_settings)
        self.back_to_home_settings.clicked.connect(self.mostrar_pagina_principal)
        self.boton_abrir_perfil_page.clicked.connect(self.mostrar_pagina_perfil)
        self.back_to_home_profile.clicked.connect(self.mostrar_pagina_principal)
        self.ecualizador_button.clicked.connect(self.mostrar_pagina_ecualizador)
        self.about_us_button.clicked.connect(self.mostrar_pagina_about_us)
        self.support_button.clicked.connect(self.mostrar_pagina_soporte)
        self.back_to_config_about.clicked.connect(self.mostrar_pagina_settings)
        self.back_to_config_equalizer.clicked.connect(self.mostrar_pagina_settings)
        self.back_to_config_support.clicked.connect(self.mostrar_pagina_settings)
        self.all_songs_button.clicked.connect(self.mostrar_all_songs)
        self.favorite_songs_button.clicked.connect(self.mostrar_favoritas)

        self.mostrar_pagina_principal()
        self.cargar_canciones_iniciales()
        self.actualizar_progreso()

        self.lista_seleccionada = self.all_songs_list

        #Botones de la pagina perfil
        self.boton_foto_de_perfil.clicked.connect(self.abrir_foto_de_perfil)
        self.tu_nombre_button.clicked.connect(self.poner_tu_nombre)

        #Botones de soporte
        self.enviar_buttton_apoyo.clicked.connect(self.enviar_correo)
        
        # actualizar la hora
        self.timer_horalabel = QTimer(self)
        self.timer_horalabel.timeout.connect(self.update_time)
        self.timer_horalabel.start(1000)  # Actualizar cada segundo

        #conexiones ventana principal
        self.cargar_canciones_button.clicked.connect(lambda: self.agregar_archivos(self.lista_de_reproduccion, self.all_songs_list))
        icon = QIcon(os.path.join(self.basedir, "icons/icons8-reproducir-64.png"))
        self.pause_button.setIcon(icon)
        self.pause_button.setCheckable(True)
        self.pause_button.toggled.connect(self.button_toggled)
        

        #inicializar pygame y timer para el qslider principal
        pygame.mixer.init()
        self.timer = QTimer()
        self.timer.timeout.connect(self.actualizar_slider)
        
        #conexion botones para modos de reproduccion
        self.repeat_button.toggled.connect(self.on_repeat_button_toggled)
        self.shuffle_button.toggled.connect(self.on_shuffle_button_toggled)

        #conexion botones para siguiente o anterior cancion
        self.next_button.clicked.connect(lambda : self.next_song(self.lista_de_reproduccion, self.lista_seleccionada))
        self.previo_button.clicked.connect(lambda: self.cancion_anterior(self.lista_de_reproduccion, self.lista_seleccionada))

        #conectar qlistwidget para reproduccir con doble click
        self.all_songs_list.itemDoubleClicked.connect(self.reproducir_cancion_seleccionada)
        self.favorite_song_list.itemDoubleClicked.connect(self.reproducir_cancion_seleccionada)


        # Configurar el QSlider para el volumen
        self.slider_volume.setRange(0, 100)
        self.slider_volume.setValue(20)  # Volumen inicial al 50%
        self.slider_volume.valueChanged.connect(self.cambiar_volumen)

        # Configurar el botón de mute
        self.pushButton_21.setCheckable(True)
        self.pushButton_21.toggled.connect(self.mute_toggled)
        
        self.volumen_anterior = 50  # Almacenar el volumen anterior

        # Inicializar pygame mixer
        pygame.mixer.init()
        pygame.mixer.music.set_volume(self.slider_volume.value() / 100.0)
        self.update_time()

        #Mostrar widget letra y visualizador
        self.show_lyrics_button.clicked.connect(self.mostrar_letra)
        self.show_visualizer_button.clicked.connect(self.mostrar_visualizador)

        #conexion de combo para fuente de los labels
        self.fontComboBox.currentFontChanged.connect(self.cambiar_fuente)

        #conexion de spinbox para el tamaño de la letra
        self.spin_box_aumentar_letra.setRange(-5,5)
        self.spin_box_aumentar_letra.setValue(0)

        # Guardar las fuentes originales de los QLabel sin ej
        self.font_before_original = self.before_current_label_song.font()
        self.font_actual_original = self.actual_current_label_song.font()
        self.font_after_original = self.after_current_label_song.font()

        # Hacer copias de las fuentes originales para evitar modificarlas directamente
        self.font_before_original_copy = QFont(self.font_before_original)
        self.font_actual_original_copy = QFont(self.font_actual_original)
        self.font_after_original_copy = QFont(self.font_after_original)

        # Conectar el signal `valueChanged` del QSpinBox al método `cambiar_tamaño_letra`
        self.spin_box_aumentar_letra.valueChanged.connect(self.cambiar_tamaño_letra)

        #conexion de slider para moverlo
        self.slider_song.sliderPressed.connect(self.pausar_musica)
        self.slider_song.sliderReleased.connect(self.soltar_slider)
        self.posicion_absoluta = 0

        #Visualizado
        #Agregar al widget visualizador_widget
        self.visualizer = VisualizerCanvas()
        self.visualizador_layout = QVBoxLayout()
        self.visualizador_layout.addWidget(self.visualizer)
        self.visualizador_widget.setLayout(self.visualizador_layout)

        # # Timer to update the visualizer
        # self.visualizer_timer = QTimer(self)
        # self.visualizer_timer.timeout.connect(self.update_visualizer)
        # self.visualizer_timer.start(30)  
        
        # Llenar la lista de favoritos con las canciones marcadas como favoritas
        self.favorite_button.toggled.connect(lambda checked: self.agregar_a_favoritos(checked, self.lista_seleccionada))
        self.lista_seleccionada.itemSelectionChanged.connect(lambda: self.actualizar_estado_boton_favorito(self.lista_seleccionada))

        # Conectar señal de cambio de página del QStackedWidget
        self.stacked_songs.currentChanged.connect(self.actualizar_lista_seleccionada)

 
    def actualizar_lista_seleccionada(self, index):
        if self.stacked_songs.currentWidget() == self.all_songs_stack:
            self.lista_seleccionada = self.all_songs_list
        elif self.stacked_songs.currentWidget() == self.favorite_songs_stack:
            self.lista_seleccionada = self.favorite_song_list
        self.actualizar_estado_boton_favorito(self.lista_seleccionada)
        self.lista_seleccionada.clearSelection()
    
    def mostrar_all_songs(self):
        self.stacked_songs.setCurrentWidget(self.all_songs_stack)
    
    def mostrar_favoritas(self):
        self.stacked_songs.setCurrentWidget(self.favorite_songs_stack)

    ####Agregar a favoritos
    def agregar_a_favoritos(self, checked, lista_widget):
        item_seleccionado = lista_widget.currentItem()
        if item_seleccionado:
            nombre_cancion = item_seleccionado.text()
            if checked:
                # Añadir a favoritos si no está ya en la lista
                if nombre_cancion not in [self.favorite_song_list.item(i).text() for i in range(self.favorite_song_list.count())]:
                    self.favorite_song_list.addItem(nombre_cancion)
                    self.estado_favoritos[nombre_cancion] = True  # Actualizar estado
            else:
                # Eliminar de favoritos si está en la lista
                items_a_eliminar = self.favorite_song_list.findItems(nombre_cancion, Qt.MatchExactly)
                for item in items_a_eliminar:
                    self.favorite_song_list.takeItem(self.favorite_song_list.row(item))
                    self.estado_favoritos[nombre_cancion] = False  # Actualizar estado

        self.actualizar_estado_boton_favorito(lista_widget)


    def actualizar_estado_boton_favorito(self, lista_widget):
        item_seleccionado = lista_widget.currentItem()
        if item_seleccionado:
            nombre_cancion = item_seleccionado.text()
            if nombre_cancion in self.estado_favoritos:
                estado_favorito = self.estado_favoritos[nombre_cancion]
                self.favorite_button.setChecked(estado_favorito)
            else:
                self.favorite_button.setChecked(False)
        else:
            self.favorite_button.setChecked(False)
    #############



    def cargar_letra(self, ruta_archivo_lrc):
        """Carga y procesa el archivo .lrc"""
        self.letras_con_tiempos.clear()
        with open(ruta_archivo_lrc, 'r', encoding='utf-8') as f:
            for line in f:
                if line.startswith('[') and ']' in line:
                    tiempo_str, texto = line.split(']', 1)
                    tiempo_str = tiempo_str[1:]  # Eliminar el primer carácter '['
                    if ':' in tiempo_str:
                        minutos, segundos = tiempo_str.split(':', 1)
                        try:
                            tiempo = int(minutos) * 60 + float(segundos)
                            self.letras_con_tiempos[tiempo] = texto.strip()
                        except ValueError:
                            continue

    def actualizar_letra(self):
        """Actualiza los labels con la letra correspondiente a la posición actual de la canción"""
        posicion_actual = self.posicion_absoluta 
        tiempos = sorted(self.letras_con_tiempos.keys())
        letra_anterior = ""
        letra_actual = ""
        letra_siguiente = ""
        for i, tiempo in enumerate(tiempos):
            if tiempo > posicion_actual:
                if i > 0:
                    letra_anterior = self.letras_con_tiempos[tiempos[i-2]]
                letra_actual = self.letras_con_tiempos[tiempos[i-1]]
                if i < len(tiempos) - 1:
                    letra_siguiente = self.letras_con_tiempos[tiempos[i]]
                break
            letra_anterior = letra_actual
            letra_actual = self.letras_con_tiempos[tiempos[i-1]]
            if i < len(tiempos) - 1:
                letra_siguiente = self.letras_con_tiempos[tiempos[i]]

        self.before_current_label_song.setText(letra_anterior)
        self.actual_current_label_song.setText(letra_actual)
        self.after_current_label_song.setText(letra_siguiente)

        # Si no hay letra, mostrar el mensaje correspondiente
        if not self.letras_con_tiempos:
            self.before_current_label_song.setText("")
            self.actual_current_label_song.setText("Esta canción no tiene letra")
            self.after_current_label_song.setText("")


    def soltar_slider(self):
        # Extraer el valor del slider y actualizar la canción
        self.posicion_absoluta = self.slider_song.value()
        posicion_actual = self.slider_song.value()
        self.label_11.setText(f"{self.formato_tiempo(posicion_actual)}")

        # Detener el temporizador mientras se ajusta la posición de reproducción
        self.timer.stop()

        # Verificar si la música estaba en pausa antes de soltar el slider
        if pygame.mixer.music.get_busy() and pygame.mixer.music.get_pos() == 0:
            self.was_paused = True
        else:
            self.was_paused = False

        # Si la música estaba reproduciéndose antes de manipular el slider, mantenerla reproduciéndose desde la nueva posición
        if not self.was_paused:
            pygame.mixer.music.set_pos(self.posicion_absoluta)
            pygame.mixer.music.pause()
            icon = QIcon(os.path.join(self.basedir, "icons/icons8-reproducir-64.png"))
            self.pause_button.setIcon(icon)
            self.paused = True
            self.actualizar_letra()
            # Reanudar el temporizador
            self.timer.start(1000)
            self.pause_button.click()
            self.pause_button.click()

        # Comprobar si la canción ha terminado
        duracion_total = self.label_12.text()
        minutos, segundos = map(int, duracion_total.split(':'))
        duracion_total_segundos = minutos * 60 + segundos
        if posicion_actual + 1 >= duracion_total_segundos:
            self.next_song(self.lista_de_reproduccion, self.all_songs_list)

    def cambiar_volumen(self, value):
        volumen = value / 100.0
        pygame.mixer.music.set_volume(volumen)

    def mute_toggled(self, checked):
        if checked:
            self.volumen_anterior = self.slider_volume.value()
            self.slider_volume.setValue(0)
            icon = QIcon(os.path.join(self.basedir, "icons/icons8-no-audio-64.png"))
            self.pushButton_21.setIcon(icon)
        else:
            self.slider_volume.setValue(self.volumen_anterior)
            icon = QIcon(os.path.join(self.basedir, "icons/icons8-sound-50.png"))
            self.pushButton_21.setIcon(icon)

    def reproducir_cancion_seleccionada(self):
        self.reproducir_musica(self.lista_de_reproduccion, self.lista_seleccionada)
        self.posicion_absoluta = 0
    
    def on_repeat_button_toggled(self, checked):
        if checked:
            # Si el botón de bucle se activa, desactiva el botón de aleatorio
            self.shuffle_button.setChecked(False)
            self.modo_reproduccion = "bucle"
            
        else:
            self.modo_reproduccion = "secuencial"  # Si se desactiva, volver al modo secuencial
            

    def on_shuffle_button_toggled(self, checked):
        if checked:
            # Si el botón de aleatorio se activa, desactiva el botón de bucle
            self.repeat_button.setChecked(False)
            self.modo_reproduccion = "aleatorio"
            
        else:
            self.modo_reproduccion = "secuencial"  # Si se desactiva, volver al modo secuencial
            

    def next_song(self, lista_de_reproduccion, lista_widget):
        if lista_de_reproduccion:
            self.posicion_absoluta = 0
            print("Modo de reproducción:", self.modo_reproduccion)
            print("Índice actual antes del cambio:", self.indice_actual)
            if self.modo_reproduccion == "secuencial":
                self.indice_actual = (self.indice_actual + 1) % len(lista_de_reproduccion)
            elif self.modo_reproduccion == "aleatorio":
                nuevo_indice = self.indice_actual
                while nuevo_indice == self.indice_actual:
                    nuevo_indice = random.randint(0, len(lista_de_reproduccion) - 1)
                self.indice_actual = nuevo_indice
            elif self.modo_reproduccion == "bucle":
                self.detener_musica()
            lista_widget.setCurrentRow(self.indice_actual)
            print("Índice actual después del cambio:", self.indice_actual)
            self.reproducir_musica(self.lista_de_reproduccion, self.all_songs_list)

    def cancion_anterior(self, lista_de_reproduccion, lista_widget, mixer=pygame.mixer):
        if lista_de_reproduccion:
            self.posicion_absoluta = 0
            if self.modo_reproduccion == "aleatorio":
                if len(self.lista_reproducidas) <= 1:
                    return
                # Eliminar la canción actual de la lista de reproducidas
                self.lista_reproducidas.pop()
                # Establecer la canción anterior como la actual
                ruta_archivo, nombre_cancion, duracion_total = self.lista_reproducidas[-1]
                self.indice_actual = lista_de_reproduccion.index((ruta_archivo, nombre_cancion, duracion_total))
            elif self.modo_reproduccion == "bucle":
                self.detener_musica()
            else:
                self.indice_actual = (self.indice_actual - 1) % len(lista_de_reproduccion)
            lista_widget.setCurrentRow(self.indice_actual)
            self.reproducir_musica(lista_de_reproduccion, lista_widget)

    def button_toggled(self, checked):
        if checked:
            self.pausar_musica()
        else:
            self.reproducir_musica(self.lista_de_reproduccion, self.all_songs_list)

    def reproducir_musica(self, lista_de_reproduccion, lista_widget, mixer=pygame.mixer):

        if lista_de_reproduccion:
            # Detener la música actual si está reproduciéndose y no está en pausa
            if mixer.music.get_busy() and not self.paused:
            # Si la música no está en pausa, detenerla antes de reproducir una nueva canción
                self.detener_musica()

            item_seleccionado = lista_widget.currentItem()
            if item_seleccionado:
                nombre_cancion = item_seleccionado.text()
                for ruta_archivo, nombre, duracion_total in lista_de_reproduccion:
                    if nombre == nombre_cancion:

                        titulo, artista = extraer_info_cancion(ruta_archivo)
                        self.label_titulo_song.setText(titulo)
                        self.label_artista_song.setText(artista)
                        self.actualizar_posicion_texto()

                        # Cargar el archivo .lrc correspondiente
                        archivo_lrc = ruta_archivo.replace('.mp3', '.lrc')
                        if os.path.exists(archivo_lrc):
                            self.actual_current_label_song.clear()
                            self.cargar_letra(archivo_lrc)
                        else:
                            self.letras_con_tiempos.clear()
                            self.actual_current_label_song.setText("Esta canción no tiene letra")

                        # Extraer la imagen de los metadatos
                        imagen_data = extraer_imagen(ruta_archivo)
                        if imagen_data:
                            pixmap = QPixmap()
                            pixmap.loadFromData(imagen_data)
                            if not pixmap.isNull():  # Comprobar si el pixmap no es nulo
                                self.label_imagen_song.setPixmap(pixmap.scaled(QSize(60,60)))
                            else:
                                print("La imagen extraída de los metadatos es nula.")
                        else:
                            print("No se encontró ninguna imagen en los metadatos.")
                            pixmap = QPixmap(os.path.join(self.basedir, "icons/icons8-song-100.png"))
                            self.label_imagen_song.setPixmap(pixmap.scaled(QSize(60,60)))


                        if not self.paused:
                            # Cargar y reproducir la nueva canción seleccionada
                            self.posicion_absoluta = 0
                            mixer.music.load(ruta_archivo)
                            mixer.music.play()
                            self.slider_song.setRange(0, int(duracion_total))
                            self.label_12.setText(f"{self.formato_tiempo(duracion_total)}")
                            self.paused = False
                            self.timer.start(1000)
                            icon = QIcon(os.path.join(self.basedir, "icons/icons8-pause-48.png"))
                            self.pause_button.setIcon(icon)
                            #self.label_current_song.setText(nombre_cancion)  # Actualiza el nombre de la canción en la etiqueta
                            self.lista_reproducidas.append((ruta_archivo, nombre_cancion, duracion_total))
                        else:
                            # Reanudar la reproducción si estaba en pausa
                            mixer.music.unpause()
                            self.timer.start(1000)
                            self.paused = False
                            icon = QIcon(os.path.join(self.basedir, "icons/icons8-pause-48.png"))
                            self.pause_button.setIcon(icon)

    def update_visualizer(self):
        if pygame.mixer.music.get_busy():
            # Assuming `self.posicion_absoluta` gives the current playback position in seconds
            pos = self.posicion_absoluta * 1000  # Convert to milliseconds
            
            # Calculate the sample to start from
            sound = pygame.mixer.Sound(self.lista_de_reproduccion[self.indice_actual])
            sample_rate = pygame.mixer.get_init()[0]
            start_sample = int((pos / 1000) * sample_rate)
            
            # Extract raw sound data and compute FFT
            raw_data = sound.get_raw()
            if len(raw_data) > start_sample + self.visualizer.num_bars:
                samples = np.frombuffer(raw_data[start_sample:start_sample + self.visualizer.num_bars], dtype=np.int16)
                spectrum = np.abs(np.fft.fft(samples))[:self.visualizer.num_bars]
                spectrum /= np.max(spectrum) if np.max(spectrum) != 0 else 1
                self.visualizer.update_visualizer(spectrum)
            else:
                self.visualizer.update_visualizer(np.zeros(self.visualizer.num_bars))
        else:
            self.visualizer.update_visualizer(np.zeros(self.visualizer.num_bars))



    def pausar_musica(self):
        if pygame.mixer.music.get_busy():
            if not self.paused:
                pygame.mixer.music.pause()
                self.timer.stop()
                self.paused = True
                self.was_paused = True  # Registrar que la música estaba pausada antes de pausarla
                icon = QIcon(os.path.join(self.basedir, "icons/icons8-reproducir-64.png"))
                self.pause_button.setIcon(icon)
            else:
                pygame.mixer.music.unpause()
                self.timer.start(1000)
                self.paused = False
                self.was_paused = False  # Registrar que la música estaba reproduciéndose antes de reanudarla
                icon = QIcon(os.path.join(self.basedir, "icons/icons8-pause-48.png"))
                self.pause_button.setIcon(icon)
            

    def detener_musica(self):
        pygame.mixer.music.stop()
        self.timer.stop()
    
    def actualizar_slider(self):
        if pygame.mixer.music.get_busy():
            if self.posicion_absoluta is not None:
                posicion_actual = self.posicion_absoluta
                self.posicion_absoluta += 1  # Incrementar la posición absoluta cada segundo
            else:
                posicion_actual = pygame.mixer.music.get_pos() / 1000  # Convertir a segundos
            self.slider_song.setValue(int(posicion_actual))
            self.label_11.setText(f"{self.formato_tiempo(posicion_actual)}")
            
            # Convertir la duración total de la canción en segundos
            duracion_total = self.label_12.text()
            minutos, segundos = map(int, duracion_total.split(':'))
            duracion_total_segundos = minutos * 60 + segundos
            self.actualizar_letra()

            # Comprobar si la canción ha terminado
            if posicion_actual+1 >= duracion_total_segundos:
                self.next_song(self.lista_de_reproduccion, self.all_songs_list)
        else:
            self.timer.stop()

    def cargar_canciones_iniciales(self):
        # Cargar canciones predefinidas en el QListWidget
        canciones_procesadas = []
        for archivo in self.lista_de_reproduccion:
            duracion = self.obtener_duracion(archivo)
            nombre_cancion = os.path.basename(archivo)
            canciones_procesadas.append((archivo, nombre_cancion, duracion))
            self.all_songs_list.addItem(nombre_cancion)  # Mostrar el nombre de la canción en el QListWidget
        self.lista_de_reproduccion = canciones_procesadas


    def agregar_archivos(self, lista_de_reproduccion, lista_widget, file_dialog=QFileDialog, progress_dialog_class=QProgressDialog, thread_class=CargarArchivosThread):
        archivos, _ = file_dialog.getOpenFileNames(self, "Abrir Archivos de Música", "", "Archivos de Música (*.mp3 *.wav)")
        if archivos:
            self.progress_dialog = progress_dialog_class("Cargando canciones...", "Cancelar", 0, 100, self)
            self.progress_dialog.setWindowTitle("Progreso")
            self.progress_dialog.setWindowModality(Qt.WindowModal)
            self.progress_dialog.show()

            self.cargar_archivos_thread = thread_class(archivos)
            self.cargar_archivos_thread.progreso.connect(self.progress_dialog.setValue)
            self.cargar_archivos_thread.archivos_cargados.connect(lambda archivos: self.procesar_archivos_cargados(archivos, lista_de_reproduccion, lista_widget))
            if not self.paso_agregar_canciones:
                self.paso_agregar_canciones = True
                self.pasos_completados += 1
                self.checkbox_agrega_canciones.setCheckable(True)
                self.checkbox_agrega_canciones.setCheckState(Qt.Checked)
                self.checkbox_agrega_canciones.setEnabled(False)
            self.actualizar_progreso()
            self.cargar_archivos_thread.start()

    def procesar_archivos_cargados(self, archivos, lista_de_reproduccion, lista_widget):
        for archivo in archivos:
            duracion = self.obtener_duracion(archivo)
            nombre_cancion = os.path.basename(archivo)  # Obtener solo el nombre del archivo sin la ruta
            lista_de_reproduccion.append((archivo, nombre_cancion, duracion))  # Agregar la duración también
        lista_widget.addItems([os.path.basename(archivo) for archivo in archivos])  # Mostrar el nombre de la canción en el QListWidget
        self.progress_dialog.close()


    def seleccionar_cancion(self, lista_widget):
        item_seleccionado = lista_widget.currentItem()
        if item_seleccionado:
            indice_seleccionado = lista_widget.row(item_seleccionado)
            self.indice_actual = indice_seleccionado
            return indice_seleccionado
        else:
            self.all_songs_list.setCurrentRow(0)
            item_seleccionado = lista_widget.currentItem()
            indice_seleccionado = lista_widget.row(item_seleccionado)
            return indice_seleccionado

    def formato_tiempo(self, segundos):
        segundos = float(segundos)  # Convertir a flotante si es una cadena de texto
        minutos = int(segundos // 60)
        segundos = int(segundos % 60)
        return f"{minutos:02}:{segundos:02}"
    
    def obtener_duracion(self, ruta_archivo):
        sound = pygame.mixer.Sound(ruta_archivo)
        duracion = sound.get_length()
        return duracion

    def mostrar_dialogo_advertencia(self, message_box=QMessageBox):
        message_box.warning(self, "Advertencia", "Debes seleccionar una canción antes de reproducirla.")

    def actualizar_posicion_texto(self):
        #Detener el qtimer si ya hay uno existente
        if hasattr(self, "scroll_timer") and self.scroll_timer.isActive():
            self.scroll_timer.stop()
        
        #Crear o reinicar el qtimer
        self.scroll_timer = QTimer(self)
        self.scroll_timer.timeout.connect(self.scroll_text)
        self.scroll_timer.start(800)  # Velocidad de desplazamiento en milisegundos
        self.titulo_texto_original = self.label_titulo_song.text() + "     "
        self.artista_texto_original = self.label_artista_song.text() + "     "
        self.titulo_index = 0
        self.artista_index = 0

        
    def scroll_text(self):
        # Desplazamiento del título de la canción
        titulo_texto = self.titulo_texto_original
        titulo_ancho = self.label_titulo_song.fontMetrics().boundingRect(titulo_texto).width()

        if titulo_ancho > self.label_titulo_song.width():
            self.label_titulo_song.setText(titulo_texto[self.titulo_index:] + titulo_texto[:self.titulo_index])
            self.titulo_index = (self.titulo_index + 1) % len(titulo_texto)

        # Desplazamiento del artista de la canción
        artista_texto = self.artista_texto_original
        artista_ancho = self.label_artista_song.fontMetrics().boundingRect(artista_texto).width()

        if artista_ancho > self.label_artista_song.width():
            self.label_artista_song.setText(artista_texto[self.artista_index:] + artista_texto[:self.artista_index])
            self.artista_index = (self.artista_index + 1) % len(artista_texto)



    def update_time(self):
        current_time = QTime.currentTime().toString('hh:mm AP')
        self.label_hora.setText(current_time)

    def mostrar_pagina_settings(self):
        self.stackedWidget.setCurrentWidget(self.setting_page)

    def mostrar_pagina_principal(self):
        self.stackedWidget.setCurrentWidget(self.principal_page)

    def mostrar_pagina_perfil(self):
        self.stackedWidget.setCurrentWidget(self.profile_page)

    def mostrar_pagina_about_us(self):
        self.stackedWidget.setCurrentWidget(self.about_us_page)

    def mostrar_pagina_ecualizador(self):
        self.stackedWidget.setCurrentWidget(self.equalizer_page)
    
    def mostrar_pagina_soporte(self):
        self.stackedWidget.setCurrentWidget(self.support_page)



    def mostrar_visualizador(self):
        self.stackedWidget_2.setCurrentIndex(1)

    def mostrar_letra(self):
        self.stackedWidget_2.setCurrentIndex(0)

    def abrir_foto_de_perfil(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Seleccionar imagen", "", "Imágenes (*.png *.xpm *.jpg *.jpeg *.bmp *.gif)")
        if file_name:
            # Cargar la imagen original
            pixmap = QPixmap(file_name)
            # Convertir la imagen a un círculo
            size = self.boton_foto_de_perfil.size()  # Tamaño del botón de la foto de perfil
            circulo_pixmap = QPixmap(size)
            circulo_pixmap.fill(Qt.transparent)

            painter = QPainter(circulo_pixmap)
            painter.setRenderHint(QPainter.Antialiasing)
            path = QPainterPath()
            path.addEllipse(0, 0, size.width(), size.height())
            painter.setClipPath(path)
            painter.drawPixmap(0, 0, size.width(), size.height(), pixmap)
            painter.end()

            # Establecer el ícono en el botón
            icon = QIcon(circulo_pixmap)
            self.boton_abrir_perfil_page.setIcon(icon)
            self.boton_foto_de_perfil.setIcon(icon)
            
            # Verificar si se ha completado el paso de agregar foto
            if not self.paso_agregar_foto:
                self.paso_agregar_foto = True
                self.pasos_completados += 1
                self.checkbox_pon_una_foto.setCheckable(True)
                self.checkbox_pon_una_foto.setCheckState(Qt.Checked)
                self.checkbox_pon_una_foto.setEnabled(False)
            self.actualizar_progreso()

    def poner_foto_circulo(self, label, pixmap):
        size = label.size()
        circulo_pixmap = QPixmap(size)
        circulo_pixmap.fill(Qt.transparent)

        painter = QPainter(circulo_pixmap)
        painter.setRenderHint(QPainter.Antialiasing)
        path = QPainterPath()
        path.addEllipse(0, 0, size.width(), size.height())
        painter.setClipPath(path)
        painter.drawPixmap(0, 0, size.width(), size.height(), pixmap)
        painter.end()

        label.setPixmap(circulo_pixmap)


    def poner_tu_nombre(self):
        dialog = QDialog()
        dialog_ui = Ui_Dialog_nombre()
        dialog_ui.setupUi(dialog)

        dialog_ui.pushButton_aceptar.clicked.connect(lambda: self.aceptar_nombre(dialog, dialog_ui))
        dialog_ui.pushButton_cancel.clicked.connect(dialog.reject)

        dialog.exec()

    def aceptar_nombre(self, dialog, dialog_ui):
        nombre_anterior = self.tu_nombre_button.text()
        nombre = dialog_ui.lineEdit_nombre.text().strip()
        if not self.paso_agregar_nombre:
            if nombre == "":
                nombre = "TU NOMBRE"
            else:
                self.paso_agregar_nombre = True
                self.pasos_completados += 1
                self.checkbox_agrega_tu_nombre.setCheckable(True)
                self.checkbox_agrega_tu_nombre.setCheckState(Qt.Checked)
                self.checkbox_agrega_tu_nombre.setEnabled(False) 
        else:
            if nombre == "":
                nombre = nombre_anterior
        self.tu_nombre_button.setText(nombre.upper())
        self.actualizar_progreso()
        dialog.accept()

   
    def actualizar_progreso(self):
        self.progressBar.setMaximum(self.pasos_totales)
        self.progressBar.setValue(self.pasos_completados)
        if self.pasos_completados == self.pasos_totales:
            self.label_progreso_en_la_app.setText("Haz cumplido los objetivos")
        else:
            self.label_progreso_en_la_app.setText(f"Objetivos completados       {self.pasos_completados}/{self.pasos_totales}")

    
    def enviar_correo(self):
        seleccionado = self.list_apoyo.currentItem()
        texto = self.plainTextEdit_support.toPlainText().strip()
        texto_a_enviar = self.plainTextEdit_support.toPlainText()

        if seleccionado:
            asunto = seleccionado.text()
            if texto:
                destinatario = "afmartinez23a@udenar.edu.co"
                # Crear el enlace mailto
                mailto_link = f"mailto:{destinatario}?subject={asunto}&body={texto_a_enviar}"

                mailto_link = mailto_link.replace(' ', '%20')

                # Abrir el enlace en el navegador predeterminado
                webbrowser.open(mailto_link)
                self.plainTextEdit_support.clear()

            else:
                self.mostrar_warning("El texto del recuadro inferior no debe estar vacio")
        else:
            self.mostrar_warning("Debes seleccionar un asunto de la lista")
    
    def mostrar_warning(self, message):
        QMessageBox.warning(self, "Advertencia", message)

    def cambiar_tamaño_letra(self):
        valor_a_cambiar = self.spin_box_aumentar_letra.value()

        # Calcular el nuevo tamaño de la fuente sumando el valor del spinBox
        before_nuevo = max(8, min(self.font_before_original_copy.pointSize() + valor_a_cambiar, 18))
        actual_nuevo = max(15, min(self.font_actual_original_copy.pointSize() + valor_a_cambiar, 25))
        after_nuevo = max(8, min(self.font_after_original_copy.pointSize() + valor_a_cambiar, 18))

        # Si el valor_a_cambiar lleva el tamaño de la fuente actual por debajo de 15, no lo cambiamos
        if valor_a_cambiar < 0 and actual_nuevo < 15:
            return

        # Crear nuevas fuentes con los nuevos tamaños
        nueva_fuente_before = QFont(self.font_before_original)
        nueva_fuente_before.setPointSize(before_nuevo)
        nueva_fuente_actual = QFont(self.font_actual_original)
        nueva_fuente_actual.setPointSize(actual_nuevo)
        nueva_fuente_after = QFont(self.font_after_original)
        nueva_fuente_after.setPointSize(after_nuevo)

        # Establecer la nueva fuente en cada QLabel con "ej"
        self.before_current_label_song_ej.setFont(nueva_fuente_before)
        self.actual_current_label_song_ej.setFont(nueva_fuente_actual)
        self.after_current_label_song_ej.setFont(nueva_fuente_after)

        # Crear nuevas fuentes sin "ej"
        nueva_fuente_before_no_ej = QFont(nueva_fuente_before)
        nueva_fuente_actual_no_ej = QFont(nueva_fuente_actual)
        nueva_fuente_after_no_ej = QFont(nueva_fuente_after)

        # Establecer la nueva fuente en cada QLabel sin "ej"
        self.before_current_label_song.setFont(nueva_fuente_before_no_ej)
        self.actual_current_label_song.setFont(nueva_fuente_actual_no_ej)
        self.after_current_label_song.setFont(nueva_fuente_after_no_ej)

    def cambiar_fuente(self, nueva_fuente):
        # Obtener el tamaño de fuente actual
        before_size = self.before_current_label_song_ej.font().pointSize()
        actual_size = self.actual_current_label_song_ej.font().pointSize()

        # Crear una nueva fuente con el nombre seleccionado y el tamaño actual
        font_grande = QFont(nueva_fuente)
        font_grande.setPointSize(actual_size)

        font_pequeña = QFont(nueva_fuente)
        font_pequeña.setPointSize(before_size)

        # Establecer la nueva fuente en cada QLabel con ej
        self.before_current_label_song_ej.setFont(font_pequeña)
        self.actual_current_label_song_ej.setFont(font_grande)
        self.after_current_label_song_ej.setFont(font_pequeña)

        # Establecer la nueva fuente en cada QLabel sin "ej"
        self.before_current_label_song.setFont(font_pequeña)
        self.actual_current_label_song.setFont(font_grande)
        self.after_current_label_song.setFont(font_pequeña)

        #actualizar las fuentes en las variables
        self.font_before_original = self.before_current_label_song.font()
        self.font_actual_original = self.actual_current_label_song.font()
        self.font_after_original = self.after_current_label_song.font()

        # Restablecer el valor del spinbox a 0
        self.spin_box_aumentar_letra.setValue(0)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("windowsvista")
    pygame.mixer.init()
    window = MainMusicApp()
    window.show()
    sys.exit(app.exec())



    