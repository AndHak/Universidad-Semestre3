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
        self.pause_button.setCheckable(True)
        self.pause_button.toggled.connect(self.button_toggled)

        pygame.mixer.init()
        self.timer = QTimer()
        self.timer.timeout.connect(self.actualizar_slider)


        self.update_time()

    def button_toggled(self, checked):
        if checked:
            self.reproducir_musica(self.lista_de_reproduccion, self.all_songs_list)
        else:
            self.pausar_musica()

    def reproducir_musica(self, lista_de_reproduccion, lista_widget, mixer=pygame.mixer):
        if lista_de_reproduccion:
            # Detener la música actual si está reproduciéndose
            if mixer.music.get_busy():
                mixer.music.stop()

            # Obtener la canción seleccionada
            self.indice_actual = self.seleccionar_cancion(lista_widget)
            if self.indice_actual is not None:
                ruta_archivo, nombre_cancion, duracion_total = lista_de_reproduccion[self.indice_actual]

                # Cargar y reproducir la nueva canción seleccionada
                mixer.music.load(ruta_archivo)
                mixer.music.play()
                self.slider_song.setRange(0, int(duracion_total))
                self.label_12.setText(f"{self.formato_tiempo(duracion_total)}")
                self.paused = False
                self.timer.start(1000)
                icon = QIcon(os.path.join(self.basedir, "icons/icons8-pause-48.png"))
                self.pause_button.setIcon(icon)
                self.lista_reproducidas.append((ruta_archivo, nombre_cancion, duracion_total))


    def pausar_musica(self, mixer=pygame.mixer):
        if self.paused:
            mixer.music.unpause()
            icon = QIcon(os.path.join(self.basedir, "icons/icons8-pause-48.png"))
            self.pause_button.setIcon(icon)
            self.paused = False
        else:
            mixer.music.pause()
            self.paused = True
            icon = QIcon(os.path.join(self.basedir, "icons/icons8-reproducir-64.png"))
            self.pause_button.setIcon(icon)

    def actualizar_slider(self):
        if pygame.mixer.music.get_busy():
            posicion_actual = pygame.mixer.music.get_pos() / 1000
            self.slider_song.setValue(int(posicion_actual))  # Convertir a milisegundos
            self.label_11.setText(f"{self.formato_tiempo(posicion_actual)}")
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
            self.cargar_archivos_thread.start()

    def procesar_archivos_cargados(self, archivos, lista_de_reproduccion, lista_widget):
        for archivo in archivos:
            duracion = self.obtener_duracion(archivo)
            nombre_cancion = os.path.basename(archivo)  # Obtener solo el nombre del archivo sin la ruta
            lista_de_reproduccion.append((archivo, nombre_cancion, duracion))  # Agregar la duración también
        lista_widget.addItems([os.path.basename(archivo) for archivo in archivos])  # Mostrar el nombre de la canción en el QListWidget
        self.progress_dialog.close()

    def detener_musica(self, mixer=pygame.mixer, timer=None):
        mixer.music.stop()
        if timer:
            timer.stop()

    def seleccionar_cancion(self, lista_widget, message_box=QMessageBox,mixer=pygame.mixer):
        item_seleccionado = lista_widget.currentItem()
        if item_seleccionado:
            indice_seleccionado = lista_widget.row(item_seleccionado)
            self.indice_actual = indice_seleccionado
            return indice_seleccionado

        else:
            message_box.warning(self, "Advertencia", "Debes seleccionar una canción antes de reproducirla.")
            return None

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
        file_mame, _ = QFileDialog.getOpenFileName(self, "Seleccionar imagen", "", "Imágenes (*.png *.xpm *.jpg *.jpeg *.bmp *.gif)")
        if file_mame:
            nueva_foto = QIcon(file_mame)
            self.boton_abrir_perfil_page.setIcon(nueva_foto)
            self.boton_foto_de_perfil.setIcon(nueva_foto)
            if not self.paso_agregar_foto:
                self.paso_agregar_foto = True
                self.pasos_completados += 1
            self.checkbox_pon_una_foto.setCheckable(True)
            self.checkbox_pon_una_foto.setCheckState(Qt.Checked)
            self.checkbox_pon_una_foto.setEnabled(False) 
            self.actualizar_progreso()


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
        else:
            if nombre == "":
                nombre = nombre_anterior
        self.tu_nombre_button.setText(nombre.upper())
        self.checkbox_agrega_tu_nombre.setCheckable(True)
        self.checkbox_agrega_tu_nombre.setCheckState(Qt.Checked)
        self.checkbox_agrega_tu_nombre.setEnabled(False) 
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


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("windowsvista")
    pygame.mixer.init()
    window = MainMusicApp()
    window.show()
    sys.exit(app.exec())



    