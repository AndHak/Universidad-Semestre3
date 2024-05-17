from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
import sys

class Main(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Nombre app")

        icon_image = r"direccion del png"
        self.icon_window = QPixmap(icon_image)
        self.setWindowIcon(self.icon_window)

        self.resize(QSize(800, 800))

        self.root_layout = QVBoxLayout()
        self.root_layout.setContentsMargins(0,0,0,0)

        self.frame_toolbar = QFrame()
        self.frame_hojas = QFrame()
        self.frame_info_pag = QFrame()
        
        self.root_layout.addWidget(self.frame_toolbar, 20)
        self.root_layout.addWidget(self.frame_hojas, 75)
        self.root_layout.addWidget(self.frame_info_pag, 5)

        self.setup_toolbar()
        self.setup_paginas()

        self.main_widget = QWidget()
        self.main_widget.setLayout(self.root_layout)
        self.setCentralWidget(self.main_widget)
    
    def setup_toolbar(self):
        self.root_toolbar = QVBoxLayout()

        self.toolbar_buttons = QHBoxLayout()
        self.toolbar_actions = QStackedLayout()

        self.frame_buttons = QFrame()
        self.frame_buttons.setLayout(self.toolbar_buttons)
        self.frame_buttons.setStyleSheet("background-color: #184bcd")
        self.frame_actions = QFrame()
        self.frame_actions.setLayout(self.toolbar_actions)
        self.frame_actions.setStyleSheet("background-color: #ffffff")

        self.root_toolbar.addWidget(self.frame_buttons, 20)
        self.root_toolbar.addWidget(self.frame_actions, 80)


        #####Diseño del toolbar buttons
        names_buttons = ["Inicio", "Insertar", "Revisar"]
        for i in names_buttons:
            button = QPushButton()
            button.setText(i)
            self.toolbar_buttons.addWidget(button)

        self.frame_toolbar.setLayout(self.root_toolbar)

    def setup_paginas(self):
        self.root_paginas = QVBoxLayout()
        self.root_paginas.setContentsMargins(100,50,100,50)

        #Pagina
        self.hoja = QLineEdit()
        self.hoja.setStyleSheet("""
                                padding: 40px;
                                background-color: #ffffff;
                                height: 600px;
                                width: 200px;
                                border: 1px solid #a6a6a6;
                                """)
        self.root_paginas.addWidget(self.hoja)

        self.frame_hojas.setLayout(self.root_paginas)

    def setup_info(self):
        pass
        


if __name__=="__main__":
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    app.exit(app.exec())