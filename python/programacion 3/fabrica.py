#Andres Felipe Martinez Guerra (codigo: 223034091)
#SEBASTIAN DAVID ORDOÑEZ BOLAÑOS (codigo: 223034072)

from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
import sys

class Main(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Fábrica de piezas")
        self.resize(QSize(300,300))

        self.icon = QPixmap()
        self.setWindowIcon(self.icon)

        self.setup_layouts()
        self.material_actual = None
        self.total_piezas = 0
        self.peso_total = 0
        self.pesos_materiales = {}
        

    def setup_layouts(self):
        self.root_layout = QStackedLayout()

        self.pagina_frontal = QWidget()
        layout = QVBoxLayout()
        

        self.botones_radio = QGroupBox("Seleccionar Material:")
        radio_layout = QVBoxLayout()
        
        self.rb_aluminio = QRadioButton("Aluminio")
        self.rb_aluminio.toggled.connect(lambda: self.update_material('Aluminio'))
        radio_layout.addWidget(self.rb_aluminio)
        
        self.rb_madera = QRadioButton("Madera")
        self.rb_madera.toggled.connect(lambda: self.update_material('Madera'))
        radio_layout.addWidget(self.rb_madera)
        
        self.rb_vidrio = QRadioButton("Vidrio")
        self.rb_vidrio.toggled.connect(lambda: self.update_material('Vidrio'))
        radio_layout.addWidget(self.rb_vidrio)

        self.botones_radio.setLayout(radio_layout)
        layout.addWidget(self.botones_radio)
        
        # Entradas para peso y número de piezas
        self.input_peso = QLineEdit()
        self.input_peso.setPlaceholderText("Ingrese el peso en kg")
        layout.addWidget(self.input_peso)
        
        self.input_piezas = QLineEdit()
        self.input_piezas.setPlaceholderText("Ingrese el número de piezas")
        layout.addWidget(self.input_piezas)

        # Botón para calcular
        self.boton_calcular = QPushButton("Calcular")
        self.boton_calcular.clicked.connect(self.calcular_totales)
        layout.addWidget(self.boton_calcular)

        self.pagina_frontal.setLayout(layout)

        # Página de resultados
        self.pagina_resultados = QWidget()
        resultados_layout = QVBoxLayout()
        
        self.etiqueta_resultados = QLabel("Resultados:")
        resultados_layout.addWidget(self.etiqueta_resultados)
        
        self.boton_regresar = QPushButton("Regresar")
        self.boton_regresar.clicked.connect(self.mostrar_grupo_1)
        resultados_layout.addWidget(self.boton_regresar)

        self.pagina_resultados.setLayout(resultados_layout)
        
        # Agregar páginas al layout raíz
        self.root_layout.addWidget(self.pagina_frontal)
        self.root_layout.addWidget(self.pagina_resultados)

        # Establecer layout y mostrar página frontal
        widget_principal = QWidget()
        widget_principal.setLayout(self.root_layout)
        self.setCentralWidget(widget_principal)
    
    def update_material(self, material):
        if not getattr(self, f"rb_{material.lower()}").isChecked():
            self.material_actual = None
        else:
            self.material_actual = material
            self.input_peso.clear()
            self.input_piezas.clear()

    def calcular_totales(self):
        if not self.material_actual:
            QMessageBox.warning(self, "Error", "No se ha seleccionado ningún material.")
            return

        try:
            peso_por_pieza = float(self.input_peso.text())
        except ValueError:
            QMessageBox.warning(self, "Error", "Ingrese el peso por pieza.")
            return

        try:
            num_piezas = int(self.input_piezas.text())
        except ValueError:
            QMessageBox.warning(self, "Error", "Ingrese el número de piezas.")
            return

        peso_total_material = peso_por_pieza * num_piezas

        if self.material_actual in self.pesos_materiales:
            piesas_anteriores, peso_anterior = self.pesos_materiales[self.material_actual]
            self.pesos_materiales[self.material_actual] = (piesas_anteriores + num_piezas, peso_anterior + peso_total_material)
        else:
            self.pesos_materiales[self.material_actual] = (num_piezas, peso_por_pieza, peso_total_material)

        self.total_piezas += num_piezas
        self.peso_total += peso_total_material

        self.actualizar_resultados()
        self.mostrar_grupo_2()

    def actualizar_resultados(self):
        texto_resultados = f"Total de Piezas: {self.total_piezas}\nTotal Peso General: {self.peso_total} kg\n"
        for material, (piezas, peso, peso_total) in self.pesos_materiales.items():
            texto_resultados += f"{material}: Piezas = {piezas}, Peso = {peso} kg, Peso total = {peso_total} kg\n"
        self.etiqueta_resultados.setText(texto_resultados)


    def mostrar_grupo_1(self):
        self.root_layout.setCurrentIndex(0)

    def mostrar_grupo_2(self):
        self.root_layout.setCurrentIndex(1)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Main()
    ventana.show()
    sys.exit(app.exec())