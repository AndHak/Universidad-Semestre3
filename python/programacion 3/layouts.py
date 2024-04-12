from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
import sys





def get_widget_color(color, texto, color_1="white"):
    widget = QWidget()
    label = QLabel(texto, widget)

    font = label.font()
    font.setPointSize(50)
    font.setBold(True)
    

    label.setFont(font)
    widget.setAutoFillBackground(True)
    palette = widget.palette()
    palette.setColor(QPalette.Window, color)

    palette.setColor(QPalette.WindowText, color_1)

    widget.setPalette(palette)

    widget.setMinimumSize(50, 30)

    return widget



class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        
        papa_layout = QVBoxLayout(self)
        self.setLayout(papa_layout)

        contador = 1

        sub_layouts = []
        for i in range(3):
            sub_layout = QHBoxLayout()
            sub_layouts.append(sub_layout)
            papa_layout.addLayout(sub_layout)
            
            if i == 0:
                colors = ["red", "yellow"]
                for color in colors:
                    sub_layout.addWidget(get_widget_color(color, f"{contador}"))
                    contador += 1
            elif i == 1:
                color = "green"
                sub_layout.addWidget(get_widget_color(color, f"{contador}"))
                contador += 1
            elif i == 2:
                colors = ["red", "purple"]
                for j, color in enumerate(colors):
                        widget = get_widget_color(color, f"{contador}")
                        sub_layout.addWidget(widget)
                        contador += 1


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec_())
