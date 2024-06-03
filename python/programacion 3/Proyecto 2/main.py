from reproductor_de_musica_ui_ui import Ui_MainWindow
from ventana_nombre_ui import Ui_Dialog_nombre
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import sys
import os
import webbrowser


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
        self.actualizar_progreso()

        #Botones de la pagina perfil
        self.boton_foto_de_perfil.clicked.connect(self.abrir_foto_de_perfil)
        self.tu_nombre_button.clicked.connect(self.poner_tu_nombre)

        #Botones de soporte
        self.enviar_buttton_apoyo.clicked.connect(self.enviar_correo)
        
        # actualizar la hora
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)  # Actualizar cada segundo

        #Cambiar ejemplo de 

        self.update_time()

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
    window = MainMusicApp()
    window.show()
    sys.exit(app.exec())



    