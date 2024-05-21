import sys
import os
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QHBoxLayout, QVBoxLayout, QWidget, QFrame
from PySide6.QtCore import Qt, QPoint, QRect
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
        self.closeButton.setFixedSize(50, 40)
        self.minimizeButton = QPushButton()
        self.minimizeButton.setFixedSize(40, 40)
        self.maximizeButton = QPushButton()
        self.maximizeButton.setFixedSize(40, 40)

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
        margin = 5
        if pos.y() <= margin:
            if pos.x() <= margin:
                return Qt.TopLeftCorner
            elif pos.x() >= rect.width() - margin:
                return Qt.TopRightCorner
            else:
                return Qt.TopEdge
        elif pos.y() >= rect.height() - margin:
            if pos.x() <= margin:
                return Qt.BottomLeftCorner
            elif pos.x() >= rect.width() - margin:
                return Qt.BottomRightCorner
            else:
                return Qt.BottomEdge
        elif pos.x() <= margin:
            return Qt.LeftEdge
        elif pos.x() >= rect.width() - margin:
            return Qt.RightEdge
        else:
            return None

    def mouseMoveEvent(self, event: QMouseEvent):
        if event.buttons() == Qt.LeftButton and self.dragPosition is not None:
            global_pos = event.globalPosition().toPoint()
            if self.resizeMode is not None:
                rect = self.parent.geometry()
                if self.resizeMode == Qt.TopEdge:
                    rect.setTop(min(global_pos.y(), rect.bottom() - self.parent.minimumHeight()))
                elif self.resizeMode == Qt.LeftEdge:
                    rect.setLeft(min(global_pos.x(), rect.right() - self.parent.minimumWidth()))
                elif self.resizeMode == Qt.BottomEdge:
                    rect.setBottom(max(global_pos.y(), rect.top() + self.parent.minimumHeight()))
                elif self.resizeMode == Qt.RightEdge:
                    rect.setRight(max(global_pos.x(), rect.left() + self.parent.minimumWidth()))
                elif self.resizeMode == Qt.TopLeftCorner:
                    rect.setTopLeft(QPoint(min(global_pos.x(), rect.right() - self.parent.minimumWidth()),
                                        min(global_pos.y(), rect.bottom() - self.parent.minimumHeight())))
                elif self.resizeMode == Qt.TopRightCorner:
                    rect.setTopRight(QPoint(max(global_pos.x(), rect.left() + self.parent.minimumWidth()),
                                            min(global_pos.y(), rect.bottom() - self.parent.minimumHeight())))
                elif self.resizeMode == Qt.BottomLeftCorner:
                    rect.setBottomLeft(QPoint(min(global_pos.x(), rect.right() - self.parent.minimumWidth()),
                                            max(global_pos.y(), rect.top() + self.parent.minimumHeight())))
                elif self.resizeMode == Qt.BottomRightCorner:
                    rect.setBottomRight(QPoint(max(global_pos.x(), rect.left() + self.parent.minimumWidth()),
                                            max(global_pos.y(), rect.top() + self.parent.minimumHeight())))

                self.parent.setGeometry(rect)
            else:
                self.parent.move(global_pos - self.dragPosition)
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
        self.setMinimumSize(300, 200)

        self.titleBar = CustomTitleBar(self)

        self.setMouseTracking(True)
        self.titleBar.setMouseTracking(True)

        self.setWindowTitle("Name app")

        self.root_layout = QVBoxLayout()
        self.root_layout.setContentsMargins(0, 0, 0, 0)

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
        self.setCursor(QCursor(Qt.ArrowCursor))

    def enterEvent(self, event):
        self.setCursor(QCursor(Qt.ArrowCursor))

    def leaveEvent(self, event):
        self.setCursor(QCursor(Qt.ArrowCursor))

    def mouseMoveEvent(self, event):
        pos = event.position()
        rect = self.rect()
        margin = 5

        resize_mode = self.titleBar.getResizeMode(event)

        if resize_mode is not None or (event.buttons() == Qt.LeftButton and self.titleBar.resizeMode is not None):
            if resize_mode == Qt.TopEdge or self.titleBar.resizeMode == Qt.TopEdge:
                self.setCursor(QCursor(Qt.SizeVerCursor))
            elif resize_mode == Qt.LeftEdge or self.titleBar.resizeMode == Qt.LeftEdge:
                self.setCursor(QCursor(Qt.SizeHorCursor))
            elif resize_mode == Qt.BottomEdge or self.titleBar.resizeMode == Qt.BottomEdge:
                self.setCursor(QCursor(Qt.SizeVerCursor))
            elif resize_mode == Qt.RightEdge or self.titleBar.resizeMode == Qt.RightEdge:
                self.setCursor(QCursor(Qt.SizeHorCursor))
            elif resize_mode == Qt.TopLeftCorner or self.titleBar.resizeMode == Qt.TopLeftCorner:
                self.setCursor(QCursor(Qt.SizeFDiagCursor))
            elif resize_mode == Qt.TopRightCorner or self.titleBar.resizeMode == Qt.TopRightCorner:
                self.setCursor(QCursor(Qt.SizeBDiagCursor))
            elif resize_mode == Qt.BottomLeftCorner or self.titleBar.resizeMode == Qt.BottomLeftCorner:
                self.setCursor(QCursor(Qt.SizeBDiagCursor))
            elif resize_mode == Qt.BottomRightCorner or self.titleBar.resizeMode == Qt.BottomRightCorner:
                self.setCursor(QCursor(Qt.SizeFDiagCursor))
        else:
            self.setCursor(QCursor(Qt.ArrowCursor))

        self.titleBar.mouseMoveEvent(event)




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
