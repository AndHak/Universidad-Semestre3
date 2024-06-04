from reproductor_de_musica_ui_ui import Ui_MainWindow
from ventana_nombre_ui import Ui_Dialog_nombre
from cargar_archivos import CargarArchivosThread
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import sys
import os
import webbrowser
import pygame
import random



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

        #Carga de canciones
        self.lista_reproducidas = []  # Lista de canciones reproducidas
        self.indice_actual = 0
        self.paused = False
        self.modo_reproduccion = "secuencial"

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
        os.path.join(self.basedir, "songs/Cinco Noches_ Paquito Guzman (letra)(MP3_128K).mp3"),
        os.path.join(self.basedir, "songs/MI TRISTEZA  -  LUIS ALBERTO POSADA (VIDEO OFICIAL)(MP3_128K).mp3"),
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
        self.next_button.clicked.connect(lambda : self.next_song(self.lista_de_reproduccion, self.all_songs_list))
        self.previo_button.clicked.connect(lambda: self.cancion_anterior(self.lista_de_reproduccion, self.all_songs_list))

        #conectar qlistwidget para reproduccir con doble click
        self.all_songs_list.itemDoubleClicked.connect(self.reproducir_cancion_seleccionada)

        # Configurar el QSlider para el volumen
        self.slider_volume.setRange(0, 100)
        self.slider_volume.setValue(50)  # Volumen inicial al 50%
        self.slider_volume.valueChanged.connect(self.cambiar_volumen)

        # Configurar el botón de mute
        self.pushButton_21.setCheckable(True)
        self.pushButton_21.toggled.connect(self.mute_toggled)
        
        self.volumen_anterior = 50  # Almacenar el volumen anterior

        # Inicializar pygame mixer
        pygame.mixer.init()
        pygame.mixer.music.set_volume(self.slider_volume.value() / 100.0)
        self.update_time()

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
        self.reproducir_musica(self.lista_de_reproduccion, self.all_songs_list)
    
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
            if self.modo_reproduccion == "aleatorio":
                if len(self.lista_reproducidas) <= 1:
                    return
                # Eliminar la canción actual de la lista de reproducidas
                self.lista_reproducidas.pop()
                # Establecer la canción anterior como la actual
                ruta_archivo, nombre_cancion, duracion_total = self.lista_reproducidas[-1]
                self.indice_actual = lista_de_reproduccion.index((ruta_archivo, nombre_cancion, duracion_total))
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
                self.detener_musica()

            # Obtener la canción seleccionada
            self.indice_actual = self.seleccionar_cancion(lista_widget)
            if self.indice_actual is not None:
                ruta_archivo, nombre_cancion, duracion_total = lista_de_reproduccion[self.indice_actual]

                titulo, artista = self.extraer_info_cancion(ruta_archivo)
                self.label_titulo_song.setText(titulo)
                self.label_artista_song.setText(artista)

                if not self.paused:
                    # Cargar y reproducir la nueva canción seleccionada
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

    def pausar_musica(self):
        if pygame.mixer.music.get_busy():
            if not self.paused:
                pygame.mixer.music.pause()
                self.timer.stop()
                self.paused = True
                icon = QIcon(os.path.join(self.basedir, "icons/icons8-reproducir-64.png"))
                self.pause_button.setIcon(icon)
            else:
                pygame.mixer.music.unpause()
                self.timer.start(1000)
                self.paused = False
                icon = QIcon(os.path.join(self.basedir, "icons/icons8-pause-48.png"))
                self.pause_button.setIcon(icon)

    def detener_musica(self):
        pygame.mixer.music.stop()
        self.timer.stop()
    
    def actualizar_slider(self):
        if pygame.mixer.music.get_busy():
            posicion_actual = pygame.mixer.music.get_pos() / 1000  # Convertir a segundos
            self.slider_song.setValue(int(posicion_actual))
            self.label_11.setText(f"{self.formato_tiempo(posicion_actual)}")
            
            # Convertir la duración total de la canción en segundos
            duracion_total = self.label_12.text()
            minutos, segundos = map(int, duracion_total.split(':'))
            duracion_total_segundos = minutos * 60 + segundos

            # Comprobar si la canción ha terminado
            if posicion_actual+1 >= duracion_total_segundos:
                self.next_song(self.lista_de_reproduccion, self.all_songs_list)
        else:
            self.timer.stop()

    def extraer_info_cancion(self, ruta_archivo):
        #Eliminar la extension del archivo
        nombre_archivo = os.path.splitext(os.path.basename(ruta_archivo))[0]

        #separar el nombre y el artista
        partes = nombre_archivo.split(",")
        if len(partes) == 2:
            titulo = partes[0].strip()
            artista = partes[1].strip()
        else:
            #Caso para el guion
            partes = nombre_archivo.split("-")
            if len(partes) == 2:
                titulo = partes[0].strip()
                artista = partes[1].strip()
            else:
                titulo = partes[0].strip()
                artista = "Desconocido"

        return titulo, artista


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

    def mostrar_all_songs(self):
        self.stacked_songs.setCurrentWidget(self.all_songs_stack)
    
    def mostrar_favoritas(self):
        self.stacked_songs.setCurrentWidget(self.favorite_songs_stack)

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


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("windowsvista")
    pygame.mixer.init()
    window = MainMusicApp()
    window.show()
    sys.exit(app.exec())



    