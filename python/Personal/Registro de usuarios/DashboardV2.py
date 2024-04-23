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
            background: qlineargradient(
                x1: 0, y1: 0, x2: 0, y2: 1,
                stop: 0.2 rgba(45, 50, 80, 1),
                stop: 0.4 rgba(45, 50, 80, 0.86),
                stop: 0.6 rgba(45, 50, 80, 0.8),
                stop: 0.8 rgba(45, 50, 80, 0.6),
                stop: 0.9 rgba(45, 50, 80, 0.2),
                stop: 1 rgba(45, 50, 80, 0)
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

    def mostrar_ultima_pagina(self, last_label, last_button):
        if last_label == "HOME":
            self.show_page(last_label, last_button)
        elif last_label == "PLACES":
            self.show_page(last_label, last_button)
        elif last_label == "CONTACT":
            self.show_page(last_label, last_button)
        elif last_label == "ABOUT":
            self.show_page(last_label, last_button)
        elif last_label == "PROFILE":
            self.show_page(last_label, last_button)



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

        ################################## Complejidad

        self.stack_images_home = QStackedLayout()
        self.stack_images_home.setContentsMargins(0,0,0,0)
        self.stack_images_home.setSpacing(0)
        self.home_frame.setLayout(self.stack_images_home)

        ################## mapa mundi completo
        self.label_background_home = QLabel()
        self.label_background_home_layout = QVBoxLayout()
        self.label_background_home.setContentsMargins(0,0,0,0)
        self.label_background_home_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_background_home_layout.addStretch()
        self.label_background_home.setLayout(self.label_background_home_layout)

        #Cargar todas las imagenes
        self.imagen_rio_de_janeiro = QPixmap(os.path.join(self.basedir, "images_dashboard/rio_de_janeiro.jpg"))
        self.imagen_paris = QPixmap(os.path.join(self.basedir, "images_dashboard/paris.jpg"))
        
        self.stack_images_home.addWidget(self.label_background_home)

        ##############################################################

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


    #primer index del root layout
    def pagina_search(self):
        self.search_layout = QVBoxLayout()
        self.search_layout.setContentsMargins(0,0,0,0)
        self.search_layout.setSpacing(0)

        self.search_frame = QFrame()
        self.search_frame.setStyleSheet(estilo_search_frame)
        self.results_frame = QFrame()
        self.results_frame.setStyleSheet(estilo_resulst_search_page)
        self.volver_search_frame = QFrame()
        self.volver_search_frame.setStyleSheet(estilo_volver_search_page)

        self.search_layout.addWidget(self.search_frame, 30)
        self.search_layout.addWidget(self.results_frame, 65)
        self.search_layout.addWidget(self.volver_search_frame, 5)


        # Barra de búsqueda
        self.search_bar_layout = QHBoxLayout()
        self.search_bar_layout.setSpacing(15)
        self.search_bar_layout.setContentsMargins(300,0,300,0)
        self.search_bar_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.search_input = QLineEdit()
        self.search_input.setStyleSheet(estilo_barra_busqueda)
        self.search_input.setBaseSize(QSize(300, 40))
        self.search_input.setGeometry(QRect(0,0,40,400))
        self.search_input.setPlaceholderText("Ej: Colombia")
        self.search_input.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        self.search_button_page = QPushButton()
        self.imagen_lupa = QPixmap(os.path.join(self.basedir, "images_dashboard/lupa_searchpage.png"))
        self.search_button_page.setBaseSize(QSize(30, 30))
        self.search_button_page.setIconSize(QSize(30,30))
        self.search_button_page.setStyleSheet(no_fondo)
        self.search_button_page.setIcon(QIcon(self.imagen_lupa)) 
        self.search_button_page.setToolTip("Buscar") 
        self.search_button_page.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed) 
        self.search_button_page.enterEvent = self.search_button_show_lupe_white
        self.search_button_page.leaveEvent = self.search_button_leave_lupe_white

        self.search_bar_layout.addWidget(self.search_input)
        self.search_bar_layout.addWidget(self.search_button_page)
        self.search_frame.setLayout(self.search_bar_layout)

        # Cuadro de resultados
        self.results_layout = QVBoxLayout()
        self.results_layout.setContentsMargins(150, 100, 100, 150)
        self.results_layout.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
        self.results_label = QLabel("Resultados de la búsqueda:")
        self.results_list = QLabel() 

        self.results_layout.addWidget(self.results_label)
        self.results_layout.addWidget(self.results_list)

        self.results_frame.setLayout(self.results_layout)

        #Volver al home
        self.volver_search_layout = QVBoxLayout()
        self.volver_search_layout.addStretch(1)
        self.volver_search_layout.setContentsMargins(0,0,0,0)
        self.volver_search_layout.setAlignment(Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignCenter)

        self.volver_search_button = QPushButton()
        self.volver_search_button.setIcon(QPixmap(os.path.join(self.basedir, "images_dashboard/Back_button_search_page.png")))
        self.volver_search_button.clicked.connect(self.volver_search_button_funtion)
        self.volver_search_button.setIconSize(QSize(40,40))
        self.volver_search_button.setBaseSize(QSize(100,100))
        self.volver_search_button.setStyleSheet(estilo_volver_search_page)
        self.volver_search_button.enterEvent = self.volver_search_entered
        self.volver_search_button.leaveEvent = self.volver_search_leave
        self.volver_search_layout.addWidget(self.volver_search_button)

        self.volver_search_frame.setLayout(self.volver_search_layout)

        self.main_search = QWidget()
        self.main_search.setLayout(self.search_layout)
        self.root_layout.addWidget(self.main_search)

    def volver_search_entered(self, event):
        self.imagen_volver_tomate = QPixmap(os.path.join(self.basedir, "images_dashboard/Back_button_search_page_enter.png"))
        self.volver_search_button.setIcon(self.imagen_volver_tomate)

    def volver_search_leave(self, event):
        self.imagen_volver_normal = QPixmap(os.path.join(self.basedir, "images_dashboard/Back_button_search_page.png"))
        self.volver_search_button.setIcon(self.imagen_volver_normal)

    def search_button_show_lupe_white(self, event):
        self.imagen_lupa_white = QPixmap(os.path.join(self.basedir, "images_dashboard/lupa_searchpage_white.png"))
        self.search_button_page.setIcon(self.imagen_lupa_white)

    def search_button_leave_lupe_white(self, event):
        self.imagen_lupa_page = QPixmap(os.path.join(self.basedir, "images_dashboard/lupa_searchpage.png"))
        self.search_button_page.setIcon(self.imagen_lupa_page)

    def volver_search_button_funtion(self):
        self.animate_return_slide(0)




    def pagina_profile(self):
        self.profile_layout = QVBoxLayout()
        self.profile_layout.setContentsMargins(0,0,0,0)
        self.profile_frame = QFrame()

        self.profile_layout.addWidget(self.profile_frame, 100)

        self.main_profile = QWidget()
        self.main_profile.setLayout(self.profile_layout)
        self.layout_paginas.addWidget(self.main_profile)

    def pagina_mapa_mundi(self):
        #Primer layour se agrega el boron saida y en el segundo frame va a ir un stack layout que va a tener
        #un vertical layout para el boton de volver al mapa grande si el stack esta en e 1 o superior,
        #dentro del vertical abra uno hbox de sali que esta despues de un layout grid que muestra botones en el mapa
        self.mapa_mundi_layout = QVBoxLayout()
        self.mapa_mundi_layout.setContentsMargins(0, 0, 0, 0)
        self.mapa_mundi_layout.setSpacing(0)

        self.mapa_mundi_frame = QFrame()
        self.mapa_mundi_frame.setStyleSheet("background: #F8F0D9;")

        self.volver_mapa_mundi_frame = QFrame()
        self.volver_mapa_mundi_frame.setStyleSheet(estilo_volver_map_page)

        self.mapa_mundi_layout.addWidget(self.mapa_mundi_frame, 95)
        self.mapa_mundi_layout.addWidget(self.volver_mapa_mundi_frame, 5)


        ################################## Complejidad

        self.stack_continentes = QStackedLayout()
        self.stack_continentes.setContentsMargins(0,0,0,0)
        self.stack_continentes.setSpacing(0)
        self.mapa_mundi_frame.setLayout(self.stack_continentes)

        ################## mapa mundi completo
        self.label_background = QLabel()
        self.label_background_layout = QVBoxLayout()
        self.label_background.setContentsMargins(0,0,0,0)
        self.label_background_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_background_layout.addStretch()
        self.label_background.setLayout(self.label_background_layout)


        self.imagen_mapa_mundi = QPixmap(os.path.join(self.basedir, "images_dashboard/2913127.jpg"))
        current_size = QSize(self.width(), self.height())
        self.imagen_mapa_mundi = self.imagen_mapa_mundi.scaled(self.label_background.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.label_background.setPixmap(QPixmap(self.imagen_mapa_mundi))
        
        #Cargar imagen y en HD
        self.label_background.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.label_background.setAlignment(Qt.AlignCenter) 


        self.label_background.setPixmap(self.imagen_mapa_mundi)
        # Agregar frame al stack
        self.stack_continentes.addWidget(self.label_background)

        ##############################################################

        #Volver al home
        self.volver_mapa_mundi_layout = QVBoxLayout()
        self.volver_mapa_mundi_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.volver_mapa_mundi_button = QPushButton()
        self.volver_mapa_mundi_button.clicked.connect(self.volver_mapa_mundi_button_funtion)
        self.volver_mapa_mundi_button.setStyleSheet(estilo_volver_map_page)
        self.img_volver_map_normal = QPixmap(os.path.join(self.basedir, "images_dashboard/img_volver_map_normal.png"))
        self.volver_mapa_mundi_button.setIcon(self.img_volver_map_normal)
        self.volver_mapa_mundi_button.setIconSize(QSize(40,40))
        self.volver_mapa_mundi_button.setBaseSize(QSize(100,100))
        self.volver_mapa_mundi_button.enterEvent = self.volver_map_page_entered
        self.volver_mapa_mundi_button.leaveEvent = self.volver_map_page_leave

        #agregar boton al layout
        self.volver_mapa_mundi_layout.addWidget(self.volver_mapa_mundi_button)
        self.volver_mapa_mundi_frame.setLayout(self.volver_mapa_mundi_layout)

        self.main_mapa_mundi = QWidget()
        self.main_mapa_mundi.setLayout(self.mapa_mundi_layout)
        self.root_layout.addWidget(self.main_mapa_mundi)


    def volver_map_page_entered(self, event):
        self.img_volver_map_select = QPixmap(os.path.join(self.basedir, "images_dashboard/img_volver_map_select.png"))
        self.volver_mapa_mundi_button.setIcon(self.img_volver_map_select)

    def volver_map_page_leave(self, event):
        self.img_volver_map_normal = QPixmap(os.path.join(self.basedir, "images_dashboard/img_volver_map_normal.png"))
        self.volver_mapa_mundi_button.setIcon(self.img_volver_map_normal)

    
    def resizeEvent(self, event):
        super().resizeEvent(event)
        # Obtener el nuevo tamaño deseado para la imagen
        new_size = QSize(self.width(), self.height())  # Aquí puedes ajustar el tamaño que desees

        # Escalar la imagen al nuevo tamaño
        self.imagen_mapa_mundi = QPixmap(os.path.join(self.basedir, "images_dashboard/2913127.jpg"))
        self.imagen_mapa_mundi = self.imagen_mapa_mundi.scaled(new_size, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        
        # Actualizar la imagen en el label_backgraund
        self.label_background.setPixmap(QPixmap(self.imagen_mapa_mundi))


    def volver_mapa_mundi_button_funtion(self):
        self.animate_return_slide(0)





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
            self.last_selected_label = label
        elif label == "PLACES":
            self.layout_paginas.setCurrentWidget(self.main_places)
            self.background_widget.setStyleSheet("background-color: transparent;")
            button.setStyleSheet(button_pages_toolbar_selected)
            button.setProperty("isUsed", True)
            self.last_selected_button = button
            self.last_selected_label = label
        elif label == "CONTACT":
            self.layout_paginas.setCurrentWidget(self.main_contact)
            self.background_widget.setStyleSheet("background-color: transparent;")
            button.setStyleSheet(button_pages_toolbar_selected)
            button.setProperty("isUsed", True)
            self.last_selected_button = button
            self.last_selected_label = label
        elif label == "ABOUT":
            self.layout_paginas.setCurrentWidget(self.main_about_us)
            self.background_widget.setStyleSheet("background-color: transparent;")
            button.setStyleSheet(button_pages_toolbar_selected)
            button.setProperty("isUsed", True)
            self.last_selected_button = button
            self.last_selected_label = label
        elif label == "SEARCH":
            self.animate_page_slide(1)
            button.setProperty("isUsed", True)
        elif label == "PROFILE":
            self.layout_paginas.setCurrentWidget(self.main_profile)
            self.background_widget.setStyleSheet("background-color: black;")
            button.setIcon(self.profile_selec)
            self.last_selected_button = button
            self.last_selected_label = label
        elif label == "MAP":
            self.animate_page_slide(2)
            button.setProperty("isUsed", True)



    #################### Movimiento animado cambiar de tack #################################
    def animate_page_slide(self, index):
        current_widget = self.root_layout.currentWidget()  # Obtener el widget actual del root_layout
        new_widget = self.root_layout.widget(index)  # Obtener el nuevo widget correspondiente al índice

        # Posición inicial del widget actual: en pantalla
        start_pos_current = QRect(0, 0, self.width(), self.height())
        # Posición final del widget actual: fuera de pantalla hacia abajo
        end_pos_current = QRect(0, self.height(), self.width(), self.height())

        # Posición inicial del nuevo widget: fuera de pantalla arriba
        start_pos_new = QRect(0, -self.height(), self.width(), self.height())
        # Posición final del nuevo widget: en pantalla
        end_pos_new = QRect(0, 0, self.width(), self.height())

        # Mostrar el nuevo widget antes de iniciar la animación
        new_widget.show()

        # Animación para el widget actual desplazándose hacia abajo
        current_widget_animation = QPropertyAnimation(current_widget, b"geometry")
        current_widget_animation.setDuration(200)  # Duración de la animación en milisegundos
        current_widget_animation.setStartValue(start_pos_current)
        current_widget_animation.setEndValue(end_pos_current)
        current_widget_animation.setEasingCurve(QEasingCurve.Linear)  # Curva de aceleración suave

        # Animación para el nuevo widget viniendo desde arriba
        new_widget_animation = QPropertyAnimation(new_widget, b"geometry")
        new_widget_animation.setDuration(200)  # Duración de la animación en milisegundos
        new_widget_animation.setStartValue(start_pos_new)
        new_widget_animation.setEndValue(end_pos_new)       
        new_widget_animation.setEasingCurve(QEasingCurve.Linear) # Curva de aceleración suave

        # Configurar secuencia de animación para sincronizar ambas animaciones
        self.animation_group = QParallelAnimationGroup()
        self.animation_group.addAnimation(current_widget_animation)
        self.animation_group.addAnimation(new_widget_animation)

        # Conectar el fin de la animación con el cambio en el rootlayout
        self.animation_group.finished.connect(lambda: self.post_animation(index))

        # Iniciar la animación
        new_widget.setGeometry(start_pos_new)  # Establecer la posición inicial del nuevo widget
        self.animation_group.start(QPropertyAnimation.DeleteWhenStopped)

    def post_animation(self, index):
        # Establecer el nuevo widget como el widget actual en el root_layout y actualizar el índice correspondiente
        self.root_layout.setCurrentIndex(index)
        

    def animate_return_slide(self, index):
        current_widget = self.root_layout.currentWidget()  # Obtener el widget actual del root_layout
        new_widget = self.root_layout.widget(index)  # Obtener el nuevo widget correspondiente al índice

        # Posición inicial del widget actual: en pantalla
        start_pos_current = QRect(0, 0, self.width(), self.height())
        # Posición final del widget actual: fuera de pantalla hacia arriba
        end_pos_current = QRect(0, -self.height(), self.width(), self.height())

        # Posición inicial del widget de destino: fuera de pantalla abajo
        start_pos_new = QRect(0, self.height(), self.width(), self.height())
        # Posición final del widget de destino: en pantalla
        end_pos_new = QRect(0, 0, self.width(), self.height())

        # Animación para el widget actual desplazándose hacia arriba
        current_widget_animation = QPropertyAnimation(current_widget, b"geometry")
        current_widget_animation.setDuration(200)  # Duración de la animación en milisegundos
        current_widget_animation.setStartValue(start_pos_current)
        current_widget_animation.setEndValue(end_pos_current)
        current_widget_animation.setEasingCurve(QEasingCurve.OutQuad)  # Curva de aceleración suave

        # Animación para el nuevo widget viniendo desde abajo
        new_widget_animation = QPropertyAnimation(new_widget, b"geometry")
        new_widget_animation.setDuration(200)  # Duración de la animación en milisegundos
        new_widget_animation.setStartValue(start_pos_new)
        new_widget_animation.setEndValue(end_pos_new)
        new_widget_animation.setEasingCurve(QEasingCurve.OutQuad)  # Curva de aceleración suave

        # Configurar secuencia de animación para sincronizar ambas animaciones
        self.animation_group = QParallelAnimationGroup()
        self.animation_group.addAnimation(current_widget_animation)
        self.animation_group.addAnimation(new_widget_animation)

        # Conectar el fin de la animación con el cambio en el rootlayout
        self.animation_group.finished.connect(lambda: self.post_return_animation(index))

        # Iniciar la animación
        new_widget.show()  # Mostrar el nuevo widget antes de iniciar la animación
        self.animation_group.start(QPropertyAnimation.DeleteWhenStopped)

    def post_return_animation(self, index):
        # Establecer el nuevo widget como el widget actual en el root_layout y actualizar el índice correspondiente
        self.root_layout.setCurrentIndex(index)






    
if __name__ == "__main__":
    app2 = QApplication(sys.argv)
    usuario_logueado = Usuario("","","","")
    window2 = Dashboard(usuario_logueado)
    window2.show()
    sys.exit(app2.exec())
