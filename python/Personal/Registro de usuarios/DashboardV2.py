from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtMultimedia import *
from estilos_dashboard import *
from usuario import *
import pickle
import sys
import os
import re





class Dashboard(QMainWindow):

    basedir = os.path.dirname(__file__)
    primero = True


    def __init__(self, usuario_logueado):
        super().__init__()

        #Imports no tocar
        self.user = usuario_logueado
        self.last_selected_button = None

        self.setWindowTitle("Mountain agency")
        self.resize(QSize(1600, 900))

        # Definir la ruta del archivo de usuarios
        self.usuarios_file = os.path.join(self.basedir, 'datos', 'usuarios_base_data.pkl')

        # Cargar los datos al iniciar la aplicación si el archivo existe
        if os.path.exists(self.usuarios_file):
            with open(self.usuarios_file, 'rb') as archivo:
                self.usuarios_base_data = pickle.load(archivo)

        self.icon = QPixmap(os.path.join(self.basedir, "images/icon.png"))
        self.setWindowIcon(self.icon)

        self.notify_sound = QSoundEffect()
        self.notify_sound.setSource(QUrl.fromLocalFile(os.path.join(self.basedir, "sounds/notify.wav")))
        #Fin imports


        self.setup_ui()



    def setup_ui(self):
        self.root_layout = QStackedLayout()
        self.root_layout.setContentsMargins(0, 0, 0, 0)
        self.root_layout.setSpacing(0)

        self.background_widget = QFrame()
        self.background_widget.setStyleSheet("background-color: transparent;")
        self.root_layout.addWidget(self.background_widget)

        self.layout_background = QVBoxLayout()
        self.layout_background.setContentsMargins(0,0,0,0)

        
        self.background_widget.setLayout(self.layout_background)


        self.frame_toolbar = QFrame()
        self.frame_toolbar.setStyleSheet("""
            background-color: qlineargradient(
                spread: pad, 
                x1: 0, y1: 0, x2: 0, y2: 1, 
                stop: 0.2 rgba(53, 62, 121, 255), 
                stop: 0.4 rgba(53, 62, 121, 220), 
                stop: 0.6 rgba(53, 62, 121, 200),
                stop: 0.8 rgba(53, 62, 121, 150),
                stop: 0.9 rgba(53, 62, 121, 50),
                stop: 1 rgba(53, 62, 121, 0)
            );
            border: none;
        """)
        self.frame_paginas = QFrame()
        self.frame_paginas.setStyleSheet("""
                            background-color: transparent;
                            border: none;
                            """)

        self.layout_paginas = QStackedLayout()
        self.layout_paginas.setContentsMargins(0,0,0,0)
        self.pagina_home()
        self.pagina_places()
        self.pagina_contact()
        self.pagina_about_us()
        self.pagina_search()
        self.pagina_profile()
        self.pagina_mapa_mundi()

        self.layout_background.addWidget(self.frame_toolbar, 15)
        self.layout_background.addWidget(self.frame_paginas, 85)

        self.frame_paginas.setLayout(self.layout_paginas)

        self.tool_bar()

        self.mostrar_pagina_por_defecto()

        self.main_widget = QWidget()
        self.main_widget.setLayout(self.root_layout)
        self.setCentralWidget(self.main_widget)


    def mostrar_pagina_por_defecto(self):
        # Mostrar la página "HOME" por defecto
        self.show_page("HOME", self.layout_buttons_pages.itemAt(0).widget())



    def tool_bar(self):
        self.layout_toolbar = QHBoxLayout()
        self.layout_toolbar.setAlignment(Qt.AlignmentFlag.AlignTop)

        #Hacer toolbar siempre presente
        self.layout_mapa_mundi = QHBoxLayout()
        self.layout_mapa_mundi.setAlignment(Qt.AlignmentFlag.AlignLeft)

        self.layout_buttons_pages = QHBoxLayout()
        self.layout_buttons_pages.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.layout_buttons_pages.setSpacing(70)

        self.layout_social_nets = QHBoxLayout()
        self.layout_social_nets.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout_social_nets.setSpacing(20)

        self.layout_profile = QHBoxLayout()
        self.layout_profile.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.layout_profile.setContentsMargins(0,0,40,0)

        self.frame_mapa_mundi = QFrame()
        self.frame_buttons_pages = QFrame()
        self.frame_social_nets = QFrame()
        self.frame_profile = QFrame()

        for frame in [self.frame_mapa_mundi, self.frame_buttons_pages, self.frame_social_nets, self.frame_profile]:
            frame.setStyleSheet("""
                                background-color: transparent;
                                """)

        self.layout_toolbar.addWidget(self.frame_mapa_mundi, 10)
        self.layout_toolbar.addWidget(self.frame_buttons_pages, 60)
        self.layout_toolbar.addWidget(self.frame_social_nets, 20)
        self.layout_toolbar.addWidget(self.frame_profile, 10)


        #Mapa mundi
        self.mapa_mundi_button = QPushButton()
        self.imagen_map = QPixmap(os.path.join(self.basedir, "images_dashboard/map_white.png"))
        self.imagen_map_select = QPixmap(os.path.join(self.basedir, "images_dashboard/map.png"))
        self.mapa_mundi_button.setIconSize(QSize(100, 42))
        self.mapa_mundi_button.setIcon(self.imagen_map)
        self.mapa_mundi_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.mapa_mundi_button.setStyleSheet("""
                                            background-color: transparent;
                                            border: none;
                                            """)
        self.mapa_mundi_button.enterEvent = self.show_mapa_mundi_select
        self.mapa_mundi_button.leaveEvent = self.show_mapa_mundi_static
        self.mapa_mundi_button.clicked.connect(lambda label_select="MAP", button_selecct=self.mapa_mundi_button: self.show_page(label_select, button_selecct))


        self.layout_mapa_mundi.addWidget(self.mapa_mundi_button)
        self.frame_mapa_mundi.setLayout(self.layout_mapa_mundi)


        # Botones
        labels = ["HOME", "PLACES", "CONTACT", "ABOUT"]
        for label in labels:
            self.crear_boton(label)


        #Lupa
        self.imagen_lupa = QPixmap(os.path.join(self.basedir, "images_dashboard/lupa.png"))
        self.imagen_lupa_animated = QMovie(os.path.join(self.basedir, "images_dashboard/lupah.gif"))
        self.imagen_lupa_animated.frameChanged.connect(self.update_lupa_icon)
        self.serach_button = QPushButton()
        self.icon_lupa = QIcon(self.imagen_lupa)
        self.serach_button.setIcon(self.icon_lupa)
        self.serach_button.setIconSize(QSize(40, 40))
        self.serach_button.enterEvent = self.show_lupa_animated
        self.serach_button.leaveEvent = self.show_lupa_static
        self.serach_button.clicked.connect(lambda label_select="SEARCH", button_selecct=self.serach_button: self.show_page(label_select, button_selecct))
        self.layout_buttons_pages.addWidget(self.serach_button)
        self.frame_buttons_pages.setLayout(self.layout_buttons_pages)


        #Social media

        # Cargar imágenes y animaciones
        self.facebook_imagen = QPixmap(os.path.join(self.basedir, "images_dashboard/f.png"))
        self.facebook_animated = QMovie(os.path.join(self.basedir, "images_dashboard/fh.gif"))
        self.facebook_animated.frameChanged.connect(self.update_facebook_icon)
        self.instagram_imagen = QPixmap(os.path.join(self.basedir, "images_dashboard/ig.png"))
        self.instagram_animated = QMovie(os.path.join(self.basedir, "images_dashboard/igh.gif"))
        self.instagram_animated.frameChanged.connect(self.update_instagram_icon)

        # Crear botones
        self.facebook_button = QPushButton()
        self.facebook_icon = QIcon(self.facebook_imagen)
        self.facebook_button.setIcon(self.facebook_icon)
        self.facebook_button.setIconSize(QSize(50, 50))
        self.facebook_button.enterEvent = self.show_facebook_animated
        self.facebook_button.leaveEvent = self.show_facebook_static
        self.facebook_button.clicked.connect(self.open_facebook_link)

        self.instagram_button = QPushButton()
        self.instagram_icon = QIcon(self.instagram_imagen)
        self.instagram_button.setIcon(self.instagram_icon)
        self.instagram_button.setIconSize(QSize(50, 50))
        self.instagram_button.enterEvent = self.show_instagram_animated
        self.instagram_button.leaveEvent = self.show_instagram_static
        self.instagram_button.clicked.connect(self.open_instagram_link)

        self.layout_social_nets.addWidget(self.facebook_button)
        self.layout_social_nets.addWidget(self.instagram_button)

        self.frame_social_nets.setLayout(self.layout_social_nets)


        #Profile
        self.profile_imagen = QPixmap(os.path.join(self.basedir, "images_dashboard/user.png"))
        self.profile_animated = QMovie(os.path.join(self.basedir, "images_dashboard/user_hover.gif"))
        self.profile_selec = QPixmap(os.path.join(self.basedir, "images_dashboard/user_selec.png"))
        self.profile_animated.frameChanged.connect(self.update_profile_icon)

        self.profile_button = QPushButton()
        self.profile_icon = QIcon(self.profile_imagen)
        self.profile_button.setIcon(self.profile_icon)
        self.profile_button.setIconSize(QSize(50, 50))
        self.profile_button.enterEvent = self.show_profile_animated
        self.profile_button.leaveEvent = self.show_profile_static
        self.profile_button.clicked.connect(lambda label_select="PROFILE", button_selecct=self.profile_button: self.show_page(label_select, button_selecct))

        self.layout_profile.addWidget(self.profile_button)
        self.frame_profile.setLayout(self.layout_profile)


        self.frame_toolbar.setLayout(self.layout_toolbar)
    
    def crear_boton(self, label):
        button = QPushButton()
        button.setText(label)
        button.setStyleSheet(button_pages_toolbar)
        button.setProperty("isUsed", False)
        self.layout_buttons_pages.addWidget(button)

        button.clicked.connect(lambda label_select=label, button_selecct=button: self.show_page(label_select, button_selecct))



    def show_mapa_mundi_select(self, event):
        self.mapa_mundi_button.setIcon(self.imagen_map_select)

    def show_mapa_mundi_static(self, event):
        self.mapa_mundi_button.setIcon(self.imagen_map)

    #Efectos para la lupa
    def show_lupa_animated(self, event):
        self.imagen_lupa_animated.start()

    def show_lupa_static(self, event):
        self.imagen_lupa_animated.stop()
        self.lupa_icon = QIcon(self.imagen_lupa)
        self.serach_button.setIcon(self.lupa_icon)

    def update_lupa_icon(self):
        self.lupa_icon = QIcon(self.imagen_lupa_animated.currentPixmap())
        self.serach_button.setIcon(self.lupa_icon)


    #Efectos para el boton facebook
    def show_facebook_animated(self, event):
        self.facebook_animated.start()

    def show_facebook_static(self, event):
        self.facebook_animated.stop()
        self.facebook_icon = QIcon(self.facebook_imagen)
        self.facebook_button.setIcon(self.facebook_icon)

    def update_facebook_icon(self):
        self.facebook_icon = QIcon(self.facebook_animated.currentPixmap())
        self.facebook_button.setIcon(self.facebook_icon)

    def open_facebook_link(self):
        QDesktopServices.openUrl(QUrl("https://www.facebook.com/YoAndHak/"))


    #Efectos para el boton instagram
    def show_instagram_animated(self, event):
        self.instagram_animated.start()

    def show_instagram_static(self, event):
        self.instagram_animated.stop()
        self.instagram_icon = QIcon(self.instagram_imagen)
        self.instagram_button.setIcon(self.instagram_icon)

    def update_instagram_icon(self):
        self.instagram_icon = QIcon(self.instagram_animated.currentPixmap())
        self.instagram_button.setIcon(self.instagram_icon)

    def open_instagram_link(self):
        QDesktopServices.openUrl(QUrl("https://www.instagram.com/_andhak_/"))


    #Efectos para el boton profile
    def show_profile_animated(self, event):
        self.profile_animated.start()

    def show_profile_static(self, event):
        self.profile_animated.stop()
        self.profile_icon = QIcon(self.profile_imagen)
        self.profile_button.setIcon(self.profile_icon)

    def update_profile_icon(self):
        self.profile_icon = QIcon(self.profile_animated.currentPixmap())
        self.profile_button.setIcon(self.profile_icon)



    # Desarrollo de las paginas
    def pagina_home(self):
        self.home_layout = QVBoxLayout()
        self.home_layout.setContentsMargins(0,0,0,0)
        self.home_frame = QFrame()

        self.home_layout.addWidget(self.home_frame, 100)

        self.main_home = QWidget()
        self.main_home.setLayout(self.home_layout)
        self.layout_paginas.addWidget(self.main_home)

    def pagina_places(self):
        self.places_layout = QVBoxLayout()
        self.places_layout.setContentsMargins(0,0,0,0)
        self.places_frame = QFrame()

        self.places_layout.addWidget(self.places_frame, 100)

        self.main_places = QWidget()
        self.main_places.setLayout(self.places_layout)
        self.layout_paginas.addWidget(self.main_places)

    def pagina_contact(self):
        self.contact_layout = QVBoxLayout()
        self.contact_layout.setContentsMargins(0,0,0,0)
        self.contact_frame = QFrame()

        self.contact_layout.addWidget(self.contact_frame, 100)

        self.main_contact = QWidget()
        self.main_contact.setLayout(self.contact_layout)
        self.layout_paginas.addWidget(self.main_contact)

    def pagina_about_us(self):
        self.about_us_layout = QVBoxLayout()
        self.about_us_layout.setContentsMargins(0,0,0,0)
        self.about_us_frame = QFrame()

        self.about_us_layout.addWidget(self.about_us_frame, 100)

        self.main_about_us = QWidget()
        self.main_about_us.setLayout(self.about_us_layout)
        self.layout_paginas.addWidget(self.main_about_us)

    def pagina_search(self):
        self.search_layout = QVBoxLayout()
        self.search_layout.setContentsMargins(0,0,0,0)
        self.search_frame = QFrame()

        self.search_layout.addWidget(self.search_frame, 100)

        self.main_search = QWidget()
        self.main_search.setLayout(self.search_layout)
        self.layout_paginas.addWidget(self.main_search)

    def pagina_profile(self):
        self.profile_layout = QVBoxLayout()
        self.profile_layout.setContentsMargins(0,0,0,0)
        self.profile_frame = QFrame()

        self.profile_layout.addWidget(self.profile_frame, 100)

        self.main_profile = QWidget()
        self.main_profile.setLayout(self.profile_layout)
        self.layout_paginas.addWidget(self.main_profile)

    def pagina_mapa_mundi(self):
        self.map_layout = QVBoxLayout()
        self.map_layout.setContentsMargins(0, 0, 0, 0)

        self.map_frame = QFrame()
        self.imagen_fondo_map = os.path.join(self.basedir, 'images_dashboard/rio_de_janeiro.jpg')
        self.background_widget.setBackgroundRole

        self.map_layout.addWidget(self.map_frame)
        self.main_mapa_mundi = QWidget()
        self.main_mapa_mundi.setLayout(self.map_layout)
        self.root_layout.addWidget(self.main_mapa_mundi)





    # Show paginas stack
    def show_page(self, label, button):
        # Restablecer el estilo del último botón seleccionado
        if self.last_selected_button:
            if self.last_selected_button != self.mapa_mundi_button and self.last_selected_button != self.profile_button and self.last_selected_button != self.serach_button:
                self.last_selected_button.setStyleSheet(button_pages_toolbar)
            self.last_selected_button.setProperty("isUsed", False)


        # Restablecer el estilo de todos los botones
        for btn in self.layout_buttons_pages.findChildren(QPushButton):
            if btn != self.mapa_mundi_button or btn != self.profile_button or btn != self.serach_button: 
                btn.setStyleSheet(button_pages_toolbar)
            btn.setProperty("isUsed", False)

        # Mostrar la página correspondiente y resaltar el botón seleccionado
        if label == "HOME":
            self.layout_paginas.setCurrentWidget(self.main_home)
            button.setStyleSheet(button_pages_toolbar_selected)
            self.background_widget.setStyleSheet("background-color: transparent;")
            button.setProperty("isUsed", True)
            self.last_selected_button = button
        elif label == "PLACES":
            self.layout_paginas.setCurrentWidget(self.main_places)
            self.background_widget.setStyleSheet("background-color: transparent;")
            button.setStyleSheet(button_pages_toolbar_selected)
            button.setProperty("isUsed", True)
            self.last_selected_button = button
        elif label == "CONTACT":
            self.layout_paginas.setCurrentWidget(self.main_contact)
            self.background_widget.setStyleSheet("background-color: transparent;")
            button.setStyleSheet(button_pages_toolbar_selected)
            button.setProperty("isUsed", True)
            self.last_selected_button = button
        elif label == "ABOUT":
            self.layout_paginas.setCurrentWidget(self.main_about_us)
            self.background_widget.setStyleSheet("background-color: transparent;")
            button.setStyleSheet(button_pages_toolbar_selected)
            button.setProperty("isUsed", True)
            self.last_selected_button = button
        elif label == "SEARCH":
            self.layout_paginas.setCurrentWidget(self.main_search)
            self.background_widget.setStyleSheet("background-color: gray;")
            button.setProperty("isUsed", True)
            self.last_selected_button = button
        elif label == "PROFILE":
            self.layout_paginas.setCurrentWidget(self.main_profile)
            self.background_widget.setStyleSheet("background-color: black;")
            button.setIcon(self.profile_selec)
            self.last_selected_button = button
        elif label == "MAP":
            self.layout_paginas.setCurrentWidget(self.main_mapa_mundi)
            self.background_widget.setStyleSheet("background-color: black;")
            button.setProperty("isUsed", True)
            self.last_selected_button = button



    #################### Movimiento de fondo - un toque complejo #################################


    
if __name__ == "__main__":
    app2 = QApplication(sys.argv)
    usuario_logueado = Usuario("","","","")
    window2 = Dashboard(usuario_logueado)
    window2.show()
    sys.exit(app2.exec())
