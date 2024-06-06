import numpy as np
from PySide6.QtWidgets import *
from PySide6.QtGui import *


class VisualizerCanvas(QGraphicsView):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setRenderHint(QPainter.Antialiasing)
        self.setFrameStyle(QFrame.NoFrame)
        self.setBackgroundBrush(QColor(0, 0, 0))  # Fondo negro

        self.scene = QGraphicsScene()
        self.setScene(self.scene)

        self.bars = []
        self.num_bars = 32
        self.max_height = 100

        for i in range(self.num_bars):
            bar = QGraphicsRectItem()
            bar.setBrush(QColor(0, 255, 0))  # Color verde
            self.bars.append(bar)
            self.scene.addItem(bar)

    def update_visualizer(self, spectrum):
        spectrum = np.clip(spectrum, 0, 1)
        width = self.width() // self.num_bars

        for i, bar in enumerate(self.bars):
            if i < len(spectrum):
                height = spectrum[i] * self.max_height
                bar.setRect(i * width, self.height() - height, width - 2, height)
            else:
                bar.setRect(i * width, self.height(), width - 2, 0)