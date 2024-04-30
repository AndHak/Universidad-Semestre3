from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
import sys

class Main(QMainWindow):
    idiomas_seleccionados = []
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Manejo de propiedades")

        self.icon = QPixmap()
        self.setWindowIcon(self.icon)

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

        self.root_page1.addWidget(self.frame_titulo)
        self.root_page1.addWidget(self.frame_qgroups)
        self.root_page1.addWidget(self.frame_continuar)

        # Desarrollo titulo
        self.titulo_layout = QVBoxLayout()
        self.titulo_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.titulo_label = QLabel()
        self.titulo_label.setText("Holi")
        self.titulo_label.setStyleSheet("font-size: 25px;")
        self.titulo_layout.addWidget(self.titulo_label)

        self.frame_titulo.setLayout(self.titulo_layout)

        # Desarrollo QGroupBoxes
        self.qgroups_layout = QStackedLayout()
        self.qgroups_layout.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
        self.qgroups_layout.setContentsMargins(100, 20, 100, 20)
        self.group_one()
        self.group_two()

        self.show_group_1()

        # Boton continuar
        self.continue_layout = QVBoxLayout()
        self.continue_layout.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.continue_button = QPushButton("Continuar")
        self.continue_button.clicked.connect(self.evaluar)
        self.continue_layout.addWidget(self.continue_button)

        self.frame_continuar.setLayout(self.continue_layout)

        self.frame_qgroups.setLayout(self.qgroups_layout)

        self.page1_widget = QWidget()
        self.page1_widget.setLayout(self.root_page1)
        self.root_layout.addWidget(self.page1_widget)

        self.root_layout.setCurrentWidget(self.page1_widget)

    def group_one(self):
        self.titulo_label.setText("¿Cuáles idiomas te gustaría aprender?")
        self.caja1 = QVBoxLayout()
        self.caja1.addStretch(1)
        self.caja1.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)

        self.frame_caja1_checkbox_principal = QFrame()
        self.frame_caja1_checkboxes_group = QFrame()

        self.caja1.addWidget(self.frame_caja1_checkbox_principal)
        self.caja1.addWidget(self.frame_caja1_checkboxes_group)

        # Checkbox principal
        self.checkbox_principal_layout = QVBoxLayout()
        self.checkbox_principal_layout.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)

        self.choose_languajes = QCheckBox()
        self.choose_languajes.setText("Idiomas")
        self.choose_languajes.toggled.connect(self.toggle_all_languages)
        self.checkbox_principal_layout.addWidget(self.choose_languajes)
        self.frame_caja1_checkbox_principal.setLayout(self.checkbox_principal_layout)

        # Checkboxes
        self.checkboxes_layout = QVBoxLayout()
        self.checkboxes_layout.addStretch(1)
        self.checkboxes_layout.setContentsMargins(40, 0, 10, 10)
        self.checkboxes_layout.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)

        self.checkbox_english = QCheckBox()
        self.checkbox_english.setText("English")
        self.checkbox_english.toggled.connect(self.update_choose_languages)
        self.checkboxes_layout.addWidget(self.checkbox_english)

        self.checkbox_frances = QCheckBox()
        self.checkbox_frances.setText("Francés")
        self.checkbox_frances.toggled.connect(self.update_choose_languages)
        self.checkboxes_layout.addWidget(self.checkbox_frances)

        self.checkbox_portugues = QCheckBox()
        self.checkbox_portugues.setText("Portugués")
        self.checkbox_portugues.toggled.connect(self.update_choose_languages)
        self.checkboxes_layout.addWidget(self.checkbox_portugues)

        self.checkbox_italiano = QCheckBox()
        self.checkbox_italiano.setText("Italiano")
        self.checkbox_italiano.toggled.connect(self.update_choose_languages)
        self.checkboxes_layout.addWidget(self.checkbox_italiano)

        self.frame_caja1_checkboxes_group.setLayout(self.checkboxes_layout)

        self.caja1_widget = QWidget()
        self.caja1_widget.setLayout(self.caja1)
        self.qgroups_layout.addWidget(self.caja1_widget)

        self.qgroups_layout.setCurrentWidget(self.caja1_widget)

    def group_two(self):
        self.caja2 = QVBoxLayout()
        self.caja2.addStretch(1)
        self.caja2.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)

        self.frame_principal2 = QFrame()
        self.caja2.addWidget(self.frame_principal2)

        self.poner_idiomas = QVBoxLayout()
        self.label_titulo_idiomas = QLabel("Idiomas escogidos")
        self.poner_idiomas.addWidget(self.label_titulo_idiomas)

        self.frame_principal2.setLayout(self.poner_idiomas)

        self.back_button = QPushButton("Volver")
        self.back_button.clicked.connect(self.show_group_1)
        self.caja2.addWidget(self.back_button)

        self.caja2_widget = QWidget()
        self.caja2_widget.setLayout(self.caja2)
        self.qgroups_layout.addWidget(self.caja2_widget)

        self.qgroups_layout.setCurrentWidget(self.caja2_widget)

    def toggle_all_languages(self, state):
        if not state:
            self.checkbox_english.setChecked(False)
            self.checkbox_frances.setChecked(False)
            self.checkbox_portugues.setChecked(False)
            self.checkbox_italiano.setChecked(False)
    
    def update_choose_languages(self, state):
        checkbox = self.sender()
        idioma = checkbox.text()

        if state:
            if idioma not in self.idiomas_seleccionados:
                self.idiomas_seleccionados.append(idioma)
        else:
            if idioma in self.idiomas_seleccionados:
                self.idiomas_seleccionados.remove(idioma)
                if not self.idiomas_seleccionados:
                    self.toggle_all_languages(False)
            else:
                checkbox.setChecked(True)

        if self.idiomas_seleccionados:
            self.choose_languajes.setChecked(True)
        else:
            self.choose_languajes.setChecked(False)



    def evaluar(self):
        self.idiomas_seleccionados.clear()

        checkbox_english = self.checkbox_english
        checkbox_frances = self.checkbox_frances
        checkbox_portugues = self.checkbox_portugues
        checkbox_italiano = self.checkbox_italiano
        cajas_idiomas = [checkbox_english, checkbox_frances, checkbox_portugues, checkbox_italiano]

        for checkbox in cajas_idiomas:
            if checkbox.isChecked():
                self.idiomas_seleccionados.append(checkbox.text())

        if self.idiomas_seleccionados:
            self.show_group_2()
        else:
            QMessageBox.warning(self, "Error", "Seleccione al menos un idioma")

    def show_group_1(self):
        self.qgroups_layout.setCurrentIndex(0)

    def show_group_2(self):
        self.qgroups_layout.setCurrentIndex(1)
        self.update_idiomas_list()

    def update_idiomas_list(self):
        idiomas_layout = QVBoxLayout()
        for i, idioma in enumerate(self.idiomas_seleccionados, start=1):
            label = QLabel()
            label.setText(f"{i}. {idioma}")
            idiomas_layout.addWidget(label)

        frame = self.frame_principal2.layout()
        while frame.count() > 1:
            item = frame.takeAt(1)
            if item is not None:
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()

        frame.addLayout(idiomas_layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec())
