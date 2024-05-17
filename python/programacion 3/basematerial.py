import sys
import os
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QHBoxLayout, QVBoxLayout, QWidget, QFrame
from PySide6.QtCore import Qt, QPoint
from PySide6.QtGui import QIcon, QCursor, QMouseEvent

class CustomTitleBar(QWidget):
    basedir = os.path.dirname(__file__)
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedHeight(40)
        self.parent = parent
        self.dragPosition = None
        self.resizeMode = None

        # Crear botones de la barra de título
        self.closeButton = QPushButton()
        self.closeButton.setFixedSize(50,40)
        self.minimizeButton = QPushButton()
        self.minimizeButton.setFixedSize(40,40)
        self.maximizeButton = QPushButton()
        self.maximizeButton.setFixedSize(40,40)

        # Configurar botones para usar íconos personalizados
        self.closeButton.setIcon(QIcon(os.path.join(self.basedir, "img/cerrar.png")))
        self.minimizeButton.setIcon(QIcon(os.path.join(self.basedir, "img/minimizar.png")))
        self.maximizeButton.setIcon(QIcon(os.path.join(self.basedir, "img/maximizar.png")))

        # Estilo de los botones
        self.closeButton.setStyleSheet(self.getCloseButtonStyle())
        self.minimizeButton.setStyleSheet(self.getButtonStyle())
        self.maximizeButton.setStyleSheet(self.getButtonStyle())

        # Conectar los botones a sus funciones
        self.closeButton.clicked.connect(self.closeWindow)
        self.minimizeButton.clicked.connect(self.minimizeWindow)
        self.maximizeButton.clicked.connect(self.maximizeWindow)

        # Diseño de los botones
        layout = QHBoxLayout()
        layout.addStretch()
        layout.addWidget(self.minimizeButton)
        layout.addWidget(self.maximizeButton)
        layout.addWidget(self.closeButton)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        self.setLayout(layout)

        # Estilo de la barra de título
        self.setStyleSheet("""
            background-color: #000000;
        """)

    def getButtonStyle(self):
        return """
        QPushButton {
            background-color: transparent;
            border: none;
        }
        QPushButton:hover {
            background-color: #3e3e3e;
        }
        """

    def getCloseButtonStyle(self):
        return """
        QPushButton {
            background-color: transparent;
            border: none;
        }
        QPushButton:hover {
            background-color: #ff4c4c;
        }
        """

    def closeWindow(self):
        self.parent.close()

    def minimizeWindow(self):
        self.parent.showMinimized()

    def maximizeWindow(self):
        if self.parent.isMaximized():
            self.parent.showNormal()
        else:
            self.parent.showMaximized()

    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.LeftButton:
            self.dragPosition = event.globalPosition().toPoint() - self.parent.frameGeometry().topLeft()
            self.resizeMode = self.getResizeMode(event)
            event.accept()

    def getResizeMode(self, event: QMouseEvent):
        rect = self.parent.rect()
        pos = event.position()
        if pos.y() <= 5:
            if pos.x() <= 5:
                return Qt.TopLeftCorner
            elif pos.x() >= rect.width() - 5:
                return Qt.TopRightCorner
            else:
                return Qt.TopEdge
        elif pos.y() >= rect.height() - 5:
            if pos.x() <= 5:
                return Qt.BottomLeftCorner
            elif pos.x() >= rect.width() - 5:
                return Qt.BottomRightCorner
            else:
                return Qt.BottomEdge
        elif pos.x() <= 5:
            return Qt.LeftEdge
        elif pos.x() >= rect.width() - 5:
            return Qt.RightEdge
        else:
            return None

    def mouseMoveEvent(self, event: QMouseEvent):
        if event.buttons() == Qt.LeftButton and self.dragPosition is not None:
            if self.resizeMode is not None:
                global_pos = event.globalPosition().toPoint()
                rect = self.parent.geometry()

                if self.resizeMode == Qt.TopEdge:
                    rect.setTop(global_pos.y() - self.dragPosition.y())
                elif self.resizeMode == Qt.LeftEdge:
                    rect.setLeft(global_pos.x() - self.dragPosition.x())
                elif self.resizeMode == Qt.BottomEdge:
                    rect.setBottom(global_pos.y())
                elif self.resizeMode == Qt.RightEdge:
                    rect.setRight(global_pos.x())
                elif self.resizeMode == Qt.TopLeftCorner:
                    rect.setTopLeft(global_pos - self.dragPosition)
                elif self.resizeMode == Qt.TopRightCorner:
                    rect.setTopRight(global_pos - self.dragPosition)
                elif self.resizeMode == Qt.BottomLeftCorner:
                    rect.setBottomLeft(global_pos - self.dragPosition)
                elif self.resizeMode == Qt.BottomRightCorner:
                    rect.setBottomRight(global_pos - self.dragPosition)

                self.parent.setGeometry(rect)
            else:
                self.parent.move(event.globalPosition().toPoint() - self.dragPosition)
            event.accept()

    def enterEvent(self, event):
        rect = self.parent.rect()
        pos = event.pos()

        # Verificar si el cursor está cerca de las esquinas para cambiar al cursor de redimensionamiento diagonal
        if pos.x() <= 5 and pos.y() <= 5:
            self.setCursor(Qt.SizeFDiagCursor)
        elif pos.x() >= rect.width() - 5 and pos.y() <= 5:
            self.setCursor(Qt.SizeBDiagCursor)
        elif pos.x() <= 5 and pos.y() >= rect.height() - 5:
            self.setCursor(Qt.SizeBDiagCursor)
        elif pos.x() >= rect.width() - 5 and pos.y() >= rect.height() - 5:
            self.setCursor(Qt.SizeFDiagCursor)
        # Cambiar el cursor a horizontal si está cerca de los bordes izquierdo o derecho
        elif pos.x() <= 5 or pos.x() >= rect.width() - 5:
            self.setCursor(Qt.SizeHorCursor)
        # Cambiar el cursor a vertical si está cerca de los bordes superior o inferior
        elif pos.y() <= 5 or pos.y() >= rect.height() - 5:
            self.setCursor(Qt.SizeVerCursor)
        else:
            # Si no está cerca de ninguna esquina 
            # o borde, usar el cursor de flecha predeterminado
            self.setCursor(Qt.ArrowCursor)

    def mouseMoveEvent(self, event: QMouseEvent):
        if event.buttons() == Qt.LeftButton and self.dragPosition is not None:
            if self.resizeMode is not None:
                global_pos = event.globalPosition().toPoint()
                rect = self.parent.geometry()

                # Calcular la diferencia entre la posición global actual y la posición del mouse en la última actualización
                diff = global_pos - self.dragPosition

                if self.resizeMode == Qt.TopEdge:
                    # Redimensionar la ventana en sentido vertical manteniendo el borde inferior fijo
                    rect.setTop(rect.top() + diff.y())
                elif self.resizeMode == Qt.LeftEdge:
                    # Redimensionar la ventana en sentido horizontal manteniendo el borde derecho fijo
                    rect.setLeft(rect.left() + diff.x())
                elif self.resizeMode == Qt.BottomEdge:
                    # Redimensionar la ventana en sentido vertical manteniendo el borde superior fijo
                    rect.setBottom(rect.bottom() + diff.y())
                elif self.resizeMode == Qt.RightEdge:
                    # Redimensionar la ventana en sentido horizontal manteniendo el borde izquierdo fijo
                    rect.setRight(rect.right() + diff.x())
                elif self.resizeMode == Qt.TopLeftCorner:
                    # Redimensionar la ventana en sentido diagonal manteniendo el borde inferior y derecho fijo
                    rect.setTop(rect.top() + diff.y())
                    rect.setLeft(rect.left() + diff.x())
                elif self.resizeMode == Qt.TopRightCorner:
                    # Redimensionar la ventana en sentido diagonal manteniendo el borde inferior y izquierdo fijo
                    rect.setTop(rect.top() + diff.y())
                    rect.setRight(rect.right() + diff.x())
                elif self.resizeMode == Qt.BottomLeftCorner:
                    # Redimensionar la ventana en sentido diagonal manteniendo el borde superior y derecho fijo
                    rect.setBottom(rect.bottom() + diff.y())
                    rect.setLeft(rect.left() + diff.x())
                elif self.resizeMode == Qt.BottomRightCorner:
                    # Redimensionar la ventana en sentido diagonal manteniendo el borde superior y izquierdo fijo
                    rect.setBottom(rect.bottom() + diff.y())
                    rect.setRight(rect.right() + diff.x())

                self.parent.setGeometry(rect)
                self.dragPosition = global_pos  # Actualizar la posición del mouse
            else:
                self.parent.move(event.globalPosition().toPoint() - self.dragPosition)
            event.accept()


    def mouseReleaseEvent(self, event: QMouseEvent):
        if event.button() == Qt.LeftButton:
            self.dragPosition = None
            self.resizeMode = None
            event.accept()


class MainWindow(QMainWindow):
    basedir = os.path.dirname(__file__)
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.FramelessWindowHint)

        self.titleBar = CustomTitleBar(self)
        self.setWindowTitle("Name app")

        self.root_layout = QVBoxLayout()
        self.root_layout.setContentsMargins(0,0,0,0)

        self.frame_barra = QFrame()
        self.frame_app_home = QFrame()

        self.root_layout.addWidget(self.frame_barra, 1)
        self.root_layout.addWidget(self.frame_app_home, 99) 

        layout = QVBoxLayout()
        layout.addWidget(self.titleBar)
        layout.addStretch()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        self.frame_barra.setLayout(layout)
        self.frame_barra.setStyleSheet("background-color: #0d0d0d")

        container = QWidget()
        container.setLayout(self.root_layout)
        self.setCentralWidget(container)

        self.desarrollo_home()

        # Estilo oscuro para la ventana
        self.setStyleSheet("""
            QMainWindow {
                background-color: #121212;
            }
        """)

    def desarrollo_home(self):
        self.root_home = QVBoxLayout()
        self.root_home.setContentsMargins(20, 20, 20, 20)
        self.root_home.setSpacing(20)

        self.frame_app_home.setLayout(self.root_home)

    def mousePressEvent(self, event):
        self.titleBar.mousePressEvent(event)

    def mouseMoveEvent(self, event):
        self.titleBar.mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        self.titleBar.mouseReleaseEvent(event)

    def enterEvent(self, event):
        self.setCursor(QCursor(Qt.ArrowCursor))

    def leaveEvent(self, event):
        self.setCursor(QCursor(Qt.ArrowCursor))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
