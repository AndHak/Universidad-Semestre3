from PySide6.QtWidgets import *


class RegistroNotas(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Ejercicio Práctico')
        self.setGeometry(300, 300, 600, 350)
        self.init_ui()

    def init_ui(self):
        layout = QHBoxLayout(self)
        self.setup_left_layout(layout)
        self.setup_right_layout(layout)

    def setup_left_layout(self, layout):
        left_layout = QVBoxLayout()
        form_layout = QFormLayout()

        self.nombre_line_edit = QLineEdit()
        form_layout.addRow('Nombre:', self.nombre_line_edit)

        edad_grado_layout = QHBoxLayout()
        self.edad_spin_box = QSpinBox()
        self.edad_spin_box.setMinimum(0)
        self.edad_spin_box.setValue(15)
        self.grado_spin_box = QSpinBox()
        self.grado_spin_box.setMinimum(9)
        self.grado_spin_box.setMaximum(11)
        self.grado_spin_box.setWrapping(True)
        edad_grado_layout.addWidget(QLabel('Edad:'))
        edad_grado_layout.addWidget(self.edad_spin_box)
        edad_grado_layout.addWidget(QLabel('Grado:'))
        edad_grado_layout.addWidget(self.grado_spin_box)

        form_layout.addRow(edad_grado_layout)
        left_layout.addLayout(form_layout)

        self.comboBox_estudiantes = QComboBox()
        self.comboBox_estudiantes.setSizeAdjustPolicy(QComboBox.AdjustToContents)
        left_layout.addWidget(self.comboBox_estudiantes)

        registrar_button = QPushButton('Registrar Estudiante')
        registrar_button.clicked.connect(self.registrar_estudiante)
        left_layout.addWidget(registrar_button)

        borrar_button = QPushButton('Borrar Estudiante')
        borrar_button.clicked.connect(self.borrar_estudiante)
        left_layout.addWidget(borrar_button)

        # Labels para mostrar los promedios
        self.promedio_9_label = QLabel('Promedio de 9°: N/A')
        left_layout.addWidget(self.promedio_9_label)

        self.promedio_10_label = QLabel('Promedio de 10°: N/A')
        left_layout.addWidget(self.promedio_10_label)

        self.promedio_11_label = QLabel('Promedio de 11°: N/A')
        left_layout.addWidget(self.promedio_11_label)

        self.promedio_total_label = QLabel('Promedio de todos los estudiantes: ')
        left_layout.addWidget(self.promedio_total_label)

        layout.addLayout(left_layout)

    def setup_right_layout(self, layout):
        right_layout = QVBoxLayout()
        self.notas = {}

        for materia in ['Español', 'Matemáticas', 'Física', 'Química']:
            nota_spin_box = QDoubleSpinBox()
            nota_spin_box.setMinimum(0)
            nota_spin_box.setMaximum(5)
            nota_spin_box.setSingleStep(0.1)
            self.notas[materia] = nota_spin_box
            right_layout.addWidget(QLabel(f'Nota {materia}:'))
            right_layout.addWidget(nota_spin_box)

        calcular_promedio_button = QPushButton('Calcular Promedio')
        calcular_promedio_button.clicked.connect(self.calcular_promedios)
        right_layout.addWidget(calcular_promedio_button)

        layout.addLayout(right_layout)

    def registrar_estudiante(self):
        nombre = self.nombre_line_edit.text()
        edad = self.edad_spin_box.value()
        grado = self.grado_spin_box.value()

        notas = {materia: nota_spin_box.value() for materia, nota_spin_box in self.notas.items()}

        promedio = sum(notas.values()) / len(notas)

        if promedio >= 3:
            resultado = 'Aprobado'
        else:
            resultado = 'Reprobado'

        estudiante_info = f"Nombre: {nombre}, Edad: {edad}, Grado: {grado}, Promedio: {promedio:.2f}, Resultado: {resultado}"

        self.comboBox_estudiantes.addItem(estudiante_info)

    def borrar_estudiante(self):
        index = self.comboBox_estudiantes.currentIndex()
        if index != -1:
            self.comboBox_estudiantes.removeItem(index)

    def calcular_promedios(self):
        total_estudiantes = self.comboBox_estudiantes.count()

        if total_estudiantes == 0:
            self.promedio_9_label.setText('Promedio de 9°: N/A')
            self.promedio_10_label.setText('Promedio de 10°: N/A')
            self.promedio_11_label.setText('Promedio de 11°: N/A')
            self.promedio_total_label.setText('Promedio de todos los estudiantes: N/A')
            return

        promedios_por_grado = {9: [], 10: [], 11: []}
        promedio_total = 0

        for i in range(total_estudiantes):
            estudiante_info = self.comboBox_estudiantes.itemText(i)
            grado = int(estudiante_info.split(',')[2].split(': ')[1])
            promedio_inicio = estudiante_info.index("Promedio: ") + len("Promedio: ")
            promedio_fin = estudiante_info.index(", Resultado:")
            promedio_estudiante = float(estudiante_info[promedio_inicio:promedio_fin])

            promedios_por_grado[grado].append(promedio_estudiante)
            promedio_total += promedio_estudiante

        for grado, promedios in promedios_por_grado.items():
            promedio = sum(promedios) / len(promedios) if promedios else None
            label = getattr(self, f"promedio_{grado}_label")
            label.setText(f'Promedio de {grado}°: {promedio:.2f}' if promedio is not None else f'Promedio de {grado}°: N/A')

        promedio_total /= total_estudiantes
        self.promedio_total_label.setText(f'Promedio de todos los estudiantes: {promedio_total:.2f}')

        for i in range(total_estudiantes):
            estudiante_info = self.comboBox_estudiantes.itemText(i)
            grado = int(estudiante_info.split(',')[2].split(": ")[1])


if __name__ == '__main__':
    app = QApplication([])
    ventana = RegistroNotas()
    ventana.show()
    app.exec()
