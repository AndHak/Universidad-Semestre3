from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
import sys

class Main(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Manejo de propiedades")

        self.icon = QPixmap()
        self.setWindowIcon(self.icon)

        self.resize(QSize(800, 900))

        self.root_layout = QStackedLayout()
        self.pagina_1()

        self.main_window = QWidget()
        self.main_window.setLayout(self.root_layout)
        self.setCentralWidget(self.main_window)

    def pagina_1(self):
        self.root_page1 = QVBoxLayout()
        
        self.frame_titulo = QFrame()
        self.frame_qgroups = QFrame()
        self.frame_continuar = QFrame()

        self.root_page1.addWidget(self.frame_titulo, 20)
        self.root_page1.addWidget(self.frame_qgroups, 60)
        self.root_page1.addWidget(self.frame_continuar, 20)

        #Desarrollo titulo
        self.titulo_layout = QVBoxLayout()
        self.titulo_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.titulo_layout.addStretch(1)

        self.titulo_label = QLabel()
        self.titulo_label.setText("Holi")
        self.titulo_label.setStyleSheet("font-size: 25px;")
        self.titulo_layout.addWidget(self.titulo_label)

        self.frame_titulo.setLayout(self.titulo_layout)

        
        #Desarrollo QGroupBoxes
        self.qgroups_layout = QStackedLayout()
        group_one()
        
        def group_one(self):
            self.caja1 = QVBoxLayout()

            self.caja1_widget = QWidget()
            self.caja1_widfet.setLayout(self.caja1)
            self.qgroups_layout.addWidget(self.caja1_widget)

            self.qgroups_layout.setCurrentWidget(self.caja1_widget)

        self.frame_qgroups.setLayout(self.qgroups_layout)


        self.page1_widget = QWidget()
        self.page1_widget.setLayout(self.root_page1)
        self.root_layout.addWidget(self.page1_widget)

        self.root_layout.setCurrentWidget(self.page1_widget)






if __name__=="__main__":
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    app.exit(app.exec())