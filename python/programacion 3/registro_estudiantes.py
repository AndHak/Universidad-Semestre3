from PySide6.QtWidgets import QApplication ,QWidget, QPushButton, QLabel, QLineEdit, QFileDialog, QMessageBox
from PySide6.QtGui import QIcon, QFont, QPixmap
import os
import sys

#validar que el usuario agrege la foto 


def apply_dark_theme(app):
    # Define el estilo CSS para el tema oscuro
    dark_stylesheet = """
    * {
        background-color: #19232D;
        color: #F0F0F0;
    }
    QPushButton {
        background-color: #38414B;
        border-style: outset;
        border-width: 2px;
        border-color: #19232D;
        border-radius: 10px;
        padding: 6px;
    }
    QPushButton:hover {
        background-color: #1ABC9C;
        color: #19232D;
    }
    QLineEdit {
        border: none;
        border-bottom: 1px solid gray;
        background-color: transparent;
        color: #F0F0F0;
        selection-background-color: #1ABC9C;
        selection-color: #F0F0F0;
    }
    """


    # Aplica el estilo CSS a la aplicación
    app.setStyleSheet(dark_stylesheet)

class MainWindow(QWidget):

    def __init__(self):

        super().__init__()

        basedir = os.path.dirname(__file__)

        self.setWindowTitle("Registro de Estudiante")
        self.setGeometry(100,100,400,250)

        icon = QIcon(os.path.join(basedir,"img", "register.png"))
        self.setWindowIcon(icon)

        label_nombre = QLabel(self)
        label_nombre.setText("Nombre")
        label_nombre.setFont(QFont("Consolas", 12))
        label_nombre.move(10,10)

        self.input_nombre = QLineEdit(self)
        self.input_nombre.setGeometry(10,35,200,20)
        self.input_nombre.setFont(QFont("Consolas", 12))

        label_edad = QLabel(self)
        label_edad.setText("Edad")
        label_edad.setFont(QFont("Consolas", 12))
        label_edad.move(10,65)

        self.input_edad = QLineEdit(self)
        self.input_edad.setGeometry(10,90,200,20)
        self.input_edad.setFont(QFont("Consolas", 12))

        label_carrera = QLabel(self)
        label_carrera.setText("Carrera que Estudia")
        label_carrera.setFont(QFont("Consolas", 12))
        label_carrera.move(10,120)

        self.input_carrera = QLineEdit(self)
        self.input_carrera.setGeometry(10,145,200,20)
        self.input_carrera.setFont(QFont("Consolas", 12))

        button_register = QPushButton(self)
        button_register.setText("Registrarse")
        button_register.setFont(QFont("Consolas", 12))
        button_register.setGeometry(10,200,200,30)
        button_register.clicked.connect(self.captura_datos)

        self.button_add_photo = QPushButton(self)
        self.button_add_photo.setText("Agregar foto")
        self.button_add_photo.setGeometry(230,150,150,30)
        self.button_add_photo.setFont(QFont("Consolas", 12))
        self.button_add_photo.clicked.connect(self.open_image_dialog)

        self.photo_label = QLabel(self)
        self.photo_label.setGeometry(230, 10, 150, 130)

    def captura_datos(self):
        nombre = self.input_nombre.text()
        edad = self.input_edad.text()
        carrera = self.input_carrera.text()
        
        # Obtener la imagen seleccionada
        try:
            with open(self.image_path, "rb") as image_file:
                image_data = image_file.read()
        except FileNotFoundError:
            QMessageBox.warning(self, "Error",
                "Debe seleccionar una imagen.",
                QMessageBox.StandardButton.Close,
                QMessageBox.StandardButton.Close)
            return

        if nombre.replace(" ", "").isalpha() and carrera.replace(" ", "").isalpha() and edad.isdigit():
            try:
                user_path = "C:\\Users\\SEBASTIAN\\OneDrive\\Documentos\\GitHub\\Tercer_Semestre_U\\usuarios.txt"
                with open(user_path, "a+") as f:
                    f.write(f"{nombre},{edad},{carrera},{self.image_path}\n")
                QMessageBox.information(self, "Creacion Exitosa",
                    "Usuario creado correctamente!",
                    QMessageBox.StandardButton.Ok,
                    QMessageBox.StandardButton.Ok)
                self.close()
            except FileNotFoundError as e:
                QMessageBox.warning(self, "Error",
                    f"La base de datos de usuario no existe:{e}",
                    QMessageBox.StandardButton.Close,
                    QMessageBox.StandardButton.Close)
        else:
            QMessageBox.warning(self, "Error Message",
                "tipos de datos no validos",
                QMessageBox.StandardButton.Close,
                QMessageBox.StandardButton.Close)


    def open_image_dialog(self):
        options = QFileDialog.Options()
        filename, _ = QFileDialog.getOpenFileName(self, "Seleccionar Imagen", "", "Archivos de Imagen (*.jpg *.png *.jpeg)", options=options)
        if filename:
            pixmap = QPixmap(filename)
            self.image_path = filename
            pixmap = pixmap.scaledToWidth(150)
            self.photo_label.setPixmap(pixmap)



        
if __name__ == "__main__":

    app = QApplication(sys.argv)
    apply_dark_theme(app)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())