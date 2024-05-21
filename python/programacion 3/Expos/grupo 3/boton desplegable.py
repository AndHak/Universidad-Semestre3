from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
import sys

class Main(QMainWindow):
    equipos = ["Liverpool", "Dortmund", "Pasto"]
    jugadores = {
        "Liverpool": [],
        "Dortmund": [],
        "Pasto": []
    }

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Nombre app")
        icon_image = r"direccion del png"
        self.icon_window = QPixmap(icon_image)
        self.setWindowIcon(self.icon_window)
        self.resize(QSize(400, 600))
        self.root_layout = QVBoxLayout()
        self.root_layout.setContentsMargins(0, 0, 0, 0)
        self.frame_principal = QFrame()
        self.root_layout.addWidget(self.frame_principal, 100)
        self.pagina_principal()
        self.main_widget = QWidget()
        self.main_widget.setLayout(self.root_layout)
        self.setCentralWidget(self.main_widget)

    def pagina_principal(self):
        self.pag1 = QVBoxLayout()
        self.label_titulo = QLabel("EQUIPOS DE FUTBOL")
        self.lista_equipos = QComboBox()
        self.lista_equipos.addItems(self.equipos)
        self.lista_equipos.currentIndexChanged.connect(self.actualizar_jugadores)
        self.name_edit = QLineEdit()
        self.name_edit.setPlaceholderText("Nombre del jugador")
        self.agregar_jugador = QPushButton("Agregar jugador")
        self.agregar_jugador.clicked.connect(self.agregar_jugador_f)
        self.show_players = QListWidget()
        self.borrar_equipo = QPushButton("Borrar equipo")
        self.borrar_equipo.clicked.connect(self.borrar_equipo_f)
        self.borrar_jugador = QPushButton("Borrar jugador")
        self.borrar_jugador.clicked.connect(self.borrar_jugador_f)
        self.pag1.addWidget(self.label_titulo)
        self.pag1.addWidget(self.lista_equipos)
        self.pag1.addWidget(self.name_edit)
        self.pag1.addWidget(self.agregar_jugador)
        self.pag1.addWidget(self.show_players)
        self.pag1.addWidget(self.borrar_equipo)
        self.pag1.addWidget(self.borrar_jugador)
        self.frame_principal.setLayout(self.pag1)
        self.actualizar_jugadores()

    def actualizar_jugadores(self):
        equipo_seleccionado = self.lista_equipos.currentText()
        self.show_players.clear()
        for jugador in self.jugadores[equipo_seleccionado]:
            self.show_players.addItem(jugador)

    def agregar_jugador_f(self):
        equipo_seleccionado = self.lista_equipos.currentText()
        jugador = self.name_edit.text().strip()
        if jugador:
            self.jugadores[equipo_seleccionado].append(jugador)
            self.actualizar_jugadores()
            self.name_edit.clear()

    def borrar_jugador_f(self):
        equipo_seleccionado = self.lista_equipos.currentText()
        selected_items = self.show_players.selectedItems()
        for item in selected_items:
            jugador = item.text()
            self.jugadores[equipo_seleccionado].remove(jugador)
        self.actualizar_jugadores()

    def borrar_equipo_f(self):
        equipo_seleccionado = self.lista_equipos.currentText()
        if equipo_seleccionado:
            self.jugadores.pop(equipo_seleccionado)
            self.lista_equipos.removeItem(self.lista_equipos.currentIndex())
            self.actualizar_jugadores()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    app.exit(app.exec())