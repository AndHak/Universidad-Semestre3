import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QCheckBox, QFormLayout

def calcular_salario(nombre, base_salary, experience_years, languages, programming_languages, married, children, seguro_de_vida):
    calculated_salary = float(base_salary)
    if int(experience_years) > 10:
        calculated_salary += 0.10 * calculated_salary
    for language in languages:
        if language in ["Ingles", "Frances", "Italiano", "Ruso"]:
            calculated_salary += 0.02 * calculated_salary
    for prog_lang in programming_languages:
        if prog_lang in ["Python", "JavaScript"]:
            calculated_salary += 0.05 * calculated_salary
    if married:
        calculated_salary += 0.02 * calculated_salary
    if children:
        calculated_salary += 0.03 * calculated_salary
    if seguro_de_vida:
        calculated_salary -= 0.07 * calculated_salary
    return calculated_salary

class SalaryApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout(self)

        # Widgets
        form_layout = QFormLayout()
        self.name_input = QLineEdit(self)
        self.email_input = QLineEdit(self)
        self.base_salary_input = QLineEdit(self)
        self.experience_years_input = QLineEdit(self)
        self.languages_input = QLineEdit(self)
        self.programming_languages_input = QLineEdit(self)
        self.married_checkbox = QCheckBox("Casado", self)
        self.children_checkbox = QCheckBox("Tiene hijos", self)
        self.seguro_de_vida_checkbox = QCheckBox("Seguro de vida", self)
        self.calculate_button = QPushButton("Calcular Salario", self)
        self.result_label = QLabel("Resultado", self)

        form_layout.addRow("Nombre:", self.name_input)
        form_layout.addRow("Email:", self.email_input)
        form_layout.addRow("Salario Base:", self.base_salary_input)
        form_layout.addRow("Años de Experiencia:", self.experience_years_input)
        form_layout.addRow("Idiomas (separados por comas):", self.languages_input)
        form_layout.addRow("Lenguajes de Programación (separados por comas):", self.programming_languages_input)
        form_layout.addRow(self.married_checkbox)
        form_layout.addRow(self.children_checkbox)
        form_layout.addRow(self.seguro_de_vida_checkbox)

        layout.addLayout(form_layout)
        layout.addWidget(self.calculate_button)
        layout.addWidget(self.result_label)

        self.calculate_button.clicked.connect(self.on_calculate)

    def on_calculate(self):
        name = self.name_input.text()
        email = self.email_input.text()
        base_salary = float(self.base_salary_input.text())
        experience_years = self.experience_years_input.text()
        languages = self.languages_input.text().split(',')
        programming_languages = self.programming_languages_input.text().split(',')
        married = self.married_checkbox.isChecked()
        children = self.children_checkbox.isChecked()
        seguro_de_vida = self.seguro_de_vida_checkbox.isChecked()
        final_salary = calcular_salario(name, base_salary, experience_years, languages, programming_languages, married, children, seguro_de_vida)
        self.result_label.setText(f"El salario final de {name} es ${final_salary:.2f}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = SalaryApp()
    ex.show()
    sys.exit(app.exec())