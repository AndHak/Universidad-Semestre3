#Andres Felipe Martinez Guerra (223034091)


from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtMultimedia import *
import sys
import re  

def validar_email(email):
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(pattern, email) is not None

def calcular_salario(base_salary, experience_years, languages, programming_languages, married, children, seguro_de_vida):
    calculated_salary = float(base_salary)
    if int(experience_years) > 10:
        calculated_salary += 0.10 * calculated_salary
    for language in languages:
        if language in ["Ingles", "Frances", "Italiano", "Ruso"]:
            calculated_salary += 0.02 * calculated_salary
    for prog_lang in programming_languages:
        if prog_lang in ["Python", "JavaScript", "Java"]:
            calculated_salary += 0.05 * calculated_salary
    if married:
        calculated_salary += 0.02 * calculated_salary
    if children:
        calculated_salary += 0.03 * calculated_salary
    if seguro_de_vida:
        calculated_salary -= 0.07 * calculated_salary
    return calculated_salary

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculadora de Salario")

        # Agregar ícono
        icon_image = "direccion del png"
        self.icon_window = QPixmap(icon_image)
        self.setWindowIcon(self.icon_window)

        self.setup_ui()

    def setup_ui(self):
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        self.form_layout = QFormLayout()

        self.name_input = QLineEdit()
        self.form_layout.addRow("Nombre", self.name_input)

        self.date_input = QDateEdit()
        self.date_input.setCalendarPopup(True)
        self.form_layout.addRow("Fecha de Nacimiento", self.date_input)

        self.email_input = QLineEdit()
        self.form_layout.addRow("Email", self.email_input)

        self.base_salary_input = QLineEdit()
        self.form_layout.addRow("Salario base", self.base_salary_input)

        self.experience_checkbox = QCheckBox("Tiene más de 10 años de experiencia")
        self.form_layout.addRow(self.experience_checkbox)

        self.idiomas_group = QGroupBox("Idiomas que maneja")
        self.idiomas_layout = QVBoxLayout()
        self.ingles_lenguaje = QCheckBox("Ingles")
        self.frances_lenguaje = QCheckBox("Frances")
        self.italiano_lenguaje = QCheckBox("Italiano")
        self.ruso_lenguaje = QCheckBox("Ruso")
        self.idiomas_layout.addWidget(self.ingles_lenguaje)
        self.idiomas_layout.addWidget(self.frances_lenguaje)
        self.idiomas_layout.addWidget(self.italiano_lenguaje)
        self.idiomas_layout.addWidget(self.ruso_lenguaje)
        self.idiomas_group.setLayout(self.idiomas_layout)
        self.form_layout.addRow(self.idiomas_group)

        self.programming_languages_group = QGroupBox("Lenguajes de Programación")
        self.programming_languages_layout = QVBoxLayout()
        self.python_lenguaje = QCheckBox("Python")
        self.javascript_lenguaje = QCheckBox("JavaScript")
        self.java_lenguaje = QCheckBox("Java")
        self.programming_languages_layout.addWidget(self.python_lenguaje)
        self.programming_languages_layout.addWidget(self.javascript_lenguaje)
        self.programming_languages_layout.addWidget(self.java_lenguaje)
        self.programming_languages_group.setLayout(self.programming_languages_layout)
        self.form_layout.addRow(self.programming_languages_group)

        self.married_checkbox = QCheckBox("Casado")
        self.children_checkbox = QCheckBox("Tiene hijos")
        self.seguro_de_vida_checkbox = QCheckBox("Tiene seguro de vida")
        self.form_layout.addRow(self.married_checkbox)
        self.form_layout.addRow(self.children_checkbox)
        self.form_layout.addRow(self.seguro_de_vida_checkbox)

        self.calculate_button = QPushButton("Calcular")
        self.calculate_button.clicked.connect(self.on_calculate)
        self.form_layout.addRow(self.calculate_button)

        self.result_label = QLabel()
        self.form_layout.addRow("Salario calculado", self.result_label)

        self.layout.addLayout(self.form_layout)
    

    def on_calculate(self):
        nombre = self.name_input.text()
        if not nombre:
            QMessageBox.warning(self, "Error", "Ingrese un nombre")
            return

        email = self.email_input.text()
        if not validar_email(email):
            QMessageBox.warning(self, "Error", "Ingrese un correo electrónico válido")
            return

        base_salary = self.base_salary_input.text()
        if not base_salary:
            QMessageBox.warning(self, "Error", "Ingrese un salario base")
            return

        experience_years = int(self.experience_checkbox.isChecked()) * 11  
        idiomas_seleccionados = [checkbox.text() for checkbox in [self.ingles_lenguaje, self.frances_lenguaje, self.italiano_lenguaje, self.ruso_lenguaje] if checkbox.isChecked()]
        programming_languages_seleccionados = [checkbox.text() for checkbox in [self.python_lenguaje, self.javascript_lenguaje, self.java_lenguaje] if checkbox.isChecked()]
        married = self.married_checkbox.isChecked()
        children = self.children_checkbox.isChecked()
        seguro_de_vida = self.seguro_de_vida_checkbox.isChecked()

        salario_calculado = calcular_salario(float(base_salary), experience_years, idiomas_seleccionados, programming_languages_seleccionados, married, children, seguro_de_vida)

        self.result_label.setText(f"El salario calculado es: {salario_calculado:.2f}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec())
