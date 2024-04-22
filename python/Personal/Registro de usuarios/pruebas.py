from PySide6.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget, QGraphicsDropShadowEffect
from PySide6.QtCore import QObject, QEvent

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.layout_buttons_pages = QVBoxLayout(self)

        # Botones
        labels = ["HOME", "PLACES", "CONTACT", "ABOUT"]
        for label in labels:
            button = QPushButton()
            button.setText(label)
            button.setStyleSheet("background-color: white; border: 1px solid black;")
            button.installEventFilter(self)  # Instalar el filtro de eventos en este widget
            self.layout_buttons_pages.addWidget(button)

    def eventFilter(self, obj, event):
        if event.type() == QEvent.Enter:
            if isinstance(obj, QPushButton):
                shadow_effect = QGraphicsDropShadowEffect()
                shadow_effect.setBlurRadius(20)
                obj.setGraphicsEffect(shadow_effect)
        elif event.type() == QEvent.Leave:
            if isinstance(obj, QPushButton):
                obj.setGraphicsEffect(None)
        return super().eventFilter(obj, event)

app = QApplication([])
window = MyWidget()
window.resize(400, 300)
window.show()
app.exec()
