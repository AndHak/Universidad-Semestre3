from PySide6 import QtCore, QtGui, QtWidgets
import os
import sys

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.central_widget = QtWidgets.QWidget(parent=MainWindow)
        self.central_widget.setObjectName("central_widget")
        self.main_frame = QtWidgets.QFrame(parent=self.central_widget)
        self.main_frame.setGeometry(QtCore.QRect(0, 0, 801, 601))
        self.main_frame.setStyleSheet("QFrame { background-color: rgb(170, 170, 127); }")
        self.main_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.main_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.main_frame.setObjectName("main_frame")
        self.vertical_layout = QtWidgets.QVBoxLayout(self.main_frame)
        self.vertical_layout.setObjectName("vertical_layout")
        self.input_frame = QtWidgets.QFrame(parent=self.main_frame)
        self.input_frame.setStyleSheet("")
        self.input_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.input_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.input_frame.setObjectName("input_frame")
        self.line_edit = QtWidgets.QLineEdit(parent=self.input_frame)
        self.line_edit.setGeometry(QtCore.QRect(40, 80, 101, 31))
        self.line_edit.setStyleSheet("background-color: #ffffff")
        self.line_edit.setObjectName("line_edit")
        self.push_button = QtWidgets.QPushButton(parent=self.input_frame)
        self.push_button.setGeometry(QtCore.QRect(160, 80, 81, 31))
        self.push_button.setStyleSheet("QPushButton { font: 900 italic 9pt \"Segoe UI\"; background-color: rgb(255, 255, 194); }")
        self.push_button.setObjectName("push_button")
        self.image_label = QtWidgets.QLabel(parent=self.input_frame)
        self.image_label.setGeometry(QtCore.QRect(530, 30, 151, 141))
        self.image_label.setText("")
        self.basedir = os.path.dirname(__file__)
        self.image_label.setPixmap(QtGui.QPixmap(os.path.join(self.basedir, "udenar.png")))
        self.image_label.setScaledContents(True)
        self.image_label.setObjectName("image_label")
        self.vertical_layout.addWidget(self.input_frame)
        self.lcd_frame = QtWidgets.QFrame(parent=self.main_frame)
        self.lcd_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.lcd_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.lcd_frame.setObjectName("lcd_frame")
        self.lcd_display = QtWidgets.QLCDNumber(parent=self.lcd_frame)
        self.lcd_display.setGeometry(QtCore.QRect(330, 2, 411, 181))
        self.lcd_display.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.lcd_display.setObjectName("lcd_display")
        self.vertical_layout.addWidget(self.lcd_frame)
        self.radio_frame = QtWidgets.QFrame(parent=self.main_frame)
        self.radio_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.radio_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.radio_frame.setObjectName("radio_frame")
        self.radio_button_decimal = QtWidgets.QRadioButton(parent=self.radio_frame)
        self.radio_button_decimal.setGeometry(QtCore.QRect(60, 90, 89, 20))
        self.radio_button_decimal.setStyleSheet("font: 900 italic 9pt \"Segoe UI\";")
        self.radio_button_decimal.setObjectName("radio_button_decimal")
        self.radio_button_octal = QtWidgets.QRadioButton(parent=self.radio_frame)
        self.radio_button_octal.setGeometry(QtCore.QRect(240, 90, 51, 20))
        self.radio_button_octal.setStyleSheet("font: 900 italic 9pt \"Segoe UI\";")
        self.radio_button_octal.setObjectName("radio_button_octal")
        self.radio_button_binary = QtWidgets.QRadioButton(parent=self.radio_frame)
        self.radio_button_binary.setGeometry(QtCore.QRect(400, 90, 61, 20))
        self.radio_button_binary.setStyleSheet("font: 900 italic 9pt \"Segoe UI\";")
        self.radio_button_binary.setObjectName("radio_button_binary")
        self.radio_button_hexadecimal = QtWidgets.QRadioButton(parent=self.radio_frame)
        self.radio_button_hexadecimal.setGeometry(QtCore.QRect(570, 90, 89, 20))
        self.radio_button_hexadecimal.setStyleSheet("font: 900 italic 9pt \"Segoe UI\";")
        self.radio_button_hexadecimal.setObjectName("radio_button_hexadecimal")
        self.vertical_layout.addWidget(self.radio_frame)
        MainWindow.setCentralWidget(self.central_widget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Agregar conexiones de señales y slots
        self.push_button.clicked.connect(self.display_number_on_lcd)

        self.radio_button_decimal.clicked.connect(self.convert_to_decimal)
        self.radio_button_decimal.setChecked(True)
        
        self.radio_button_octal.clicked.connect(self.convert_to_octal)
        self.radio_button_binary.clicked.connect(self.convert_to_binary)
        self.radio_button_hexadecimal.clicked.connect(self.convert_to_hexadecimal)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.push_button.setText(_translate("MainWindow", "Ingresar"))
        self.radio_button_decimal.setText(_translate("MainWindow", "Decimal"))
        self.radio_button_octal.setText(_translate("MainWindow", "Octal"))
        self.radio_button_binary.setText(_translate("MainWindow", "Binario"))
        self.radio_button_hexadecimal.setText(_translate("MainWindow", "Hexadecimal"))

    def convert_to_decimal(self):
        self.display_number_on_lcd()
        value = self.lcd_display.intValue()
        self.lcd_display.display(value)
        digit_count = len(str(value))
        self.lcd_display.setDigitCount(digit_count)

    def convert_to_octal(self):
        self.display_number_on_lcd()
        value = self.lcd_display.intValue()
        octal_value = oct(value)[2:]
        self.lcd_display.display(octal_value)
        self.lcd_display.setDigitCount(len(octal_value))

    def convert_to_binary(self):
        self.display_number_on_lcd()
        value = int(self.lcd_display.intValue())

        binary_value = bin(value)[2:]  
        self.lcd_display.display(binary_value)
        self.lcd_display.setDigitCount(len(binary_value))



    def convert_to_hexadecimal(self):
        self.display_number_on_lcd()
        value = self.lcd_display.intValue()
        hexadecimal_value = hex(value)[2:].upper()
        self.lcd_display.display(hexadecimal_value)
        self.lcd_display.setDigitCount(len(hexadecimal_value))
        
    
    def display_number_on_lcd(self):
        num = self.line_edit.text().strip()
        if self.line_edit.text() == "":
            pass
        else:
            if not num.isdigit():
                self.lcd_display.display("error")
                self.lcd_display.setDigitCount(7)
            
            else:
                numero = int(self.line_edit.text())
                self.lcd_display.display(numero)
                self.lcd_display.setDigitCount(7)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())
