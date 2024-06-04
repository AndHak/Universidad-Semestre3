from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

class MarqueeLabel(QLabel):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        self.initUI()
    
    def initUI(self):
        self.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_position)
        self.timer.start(30)  # Ajusta el intervalo de tiempo para controlar la velocidad del desplazamiento
        self.pos = 0

    def update_position(self):
        self.pos -= 1
        if self.pos < -self.fontMetrics().boundingRect(self.text()).width():
            self.pos = self.width()
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(self.palette().color(QPalette.WindowText))
        rect = self.rect()
        text_width = self.fontMetrics().boundingRect(self.text()).width()
        painter.drawText(self.pos, rect.top(), text_width, rect.height(), Qt.AlignLeft | Qt.AlignVCenter, self.text())
        if self.pos + text_width < self.width():
            painter.drawText(self.pos + text_width, rect.top(), text_width, rect.height(), Qt.AlignLeft | Qt.AlignVCenter, self.text())