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


    def __init__(self, usuario_logueado):
        super().__init__()

        #Imports no tocar
        self.user = usuario_logueado

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


        self.background_images = [
            os.path.join(self.basedir, 'images_dashboard', 'rio_de_janeiro.jpg'),
            os.path.join(self.basedir, 'images_dashboard', 'paris.jpg'),
        ]

        self.effects_sombra = [QGraphicsDropShadowEffect(self) for _ in range(2)]
        self.effects_sombra[0].setBlurRadius(30)
        self.effects_sombra[1].setBlurRadius(10)
        self.effects_sombra[1].setColor(Qt.black)
        self.effects_sombra[1].setOffset(0, 0)

        self.setup_ui()

    def setup_ui(self):
        self.root_layout = QVBoxLayout()
        self.root_layout.setContentsMargins(0,0,0,0)
        self.root_layout.setSpacing(0)

        self.frame_toolbar = QFrame()
        self.frame_toolbar.setStyleSheet("""
                            background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0.2 rgba(24, 71, 127, 200), stop:0.6 rgba(24, 71, 127, 100), stop:1 rgba(24, 71, 127, 0));
                            border: none;
                            """)
        self.frame_paginas = QFrame()
        self.frame_paginas.setStyleSheet("""
                            background-color: transparent;
                            border: none;
                            """)

        self.layout_paginas = QStackedLayout()
        self.pagina_home()
        self.pagina_places()
        self.pagina_contact()
        self.pagina_about_us()
        self.pagina_profile()
        self.pagina_mapa_mundi()

        self.root_layout.addWidget(self.frame_toolbar, 15)
        self.root_layout.addWidget(self.frame_paginas, 85)

        self.tool_bar()


        self.main_widget = QWidget()
        self.main_widget.setLayout(self.root_layout)
        self.setCentralWidget(self.main_widget)

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
        mapa_mundi_icon = os.path.join(self.basedir, "images_dashboard/map_white.png")
        self.imagen_map = QPixmap(mapa_mundi_icon)
        self.mapa_mundi_button.setIcon(self.imagen_map)
        self.mapa_mundi_button.setIconSize(QSize(100, 42))
        self.mapa_mundi_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.mapa_mundi_button.setStyleSheet("""
                                            background-color: transparent;
                                            border: none;
                                            """)


        self.layout_mapa_mundi.addWidget(self.mapa_mundi_button)
        self.frame_mapa_mundi.setLayout(self.layout_mapa_mundi)


        #Efectos para el toolbar


        # Botones
        labels = ["HOME", "PLACES", "CONTACT", "ABOUT"]
        for i in range(4):
            button = QPushButton()
            button.setText(labels[i])
            button.setStyleSheet(button_pages_toolbar)
            button.setGraphicsEffect(self.effects_sombra[0])
            button.enterEvent = lambda event, button=button: button.setGraphicsEffect(self.effects_sombra[1])
            button.leaveEvent = lambda event, button=button: button.setGraphicsEffect(self.effects_sombra[0])
            self.layout_buttons_pages.addWidget(button)

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
        self.profile_animated.frameChanged.connect(self.update_profile_icon)

        self.profile_button = QPushButton()
        self.profile_icon = QIcon(self.profile_imagen)
        self.profile_button.setIcon(self.profile_icon)
        self.profile_button.setIconSize(QSize(50, 50))
        self.profile_button.enterEvent = self.show_profile_animated
        self.profile_button.leaveEvent = self.show_profile_static

        self.layout_profile.addWidget(self.profile_button)
        self.frame_profile.setLayout(self.layout_profile)


        self.frame_toolbar.setLayout(self.layout_toolbar)

    #Efectos para los botones home...
    def apply_hover_effect(self, button):
        button.setGraphicsEffect(self.effecto_sombra_hover)

    def remove_hover_effect(self, button):
        button.setGraphicsEffect(self.effecto_sombra)



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


    #Mover los indices del stacklayout
    def pagina_home(self):
        self.layout_paginas.setCurrentIndex(0)


    def pagina_places(self):
        self.layout_paginas.setCurrentIndex(1)


    def pagina_contact(self):
        self.layout_paginas.setCurrentIndex(2)


    def pagina_about_us(self):
        self.layout_paginas.setCurrentIndex(3)


    def pagina_profile(self):
        self.layout_paginas.setCurrentIndex(4)

    
    def pagina_mapa_mundi(self):
        self.layout_paginas.setCurrentIndex(5)





if __name__ == "__main__":
    app2 = QApplication(sys.argv)
    usuario_logueado = Usuario("","","","")
    window2 = Dashboard(usuario_logueado)
    window2.show()
    sys.exit(app2.exec())
