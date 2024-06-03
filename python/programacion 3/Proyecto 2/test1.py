import sys
from PySide6.QtWidgets import QApplication, QListWidget, QMainWindow, QListWidgetItem, QVBoxLayout, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Ejemplo de QListWidget con arrastrar y soltar")

        # Crear el QListWidget
        self.list_widget = QListWidget()

        # Habilitar arrastrar y soltar
        self.list_widget.setDragDropMode(QListWidget.InternalMove)

        # Agregar ítems a la lista
        for i in range(10):
            item = QListWidgetItem(f"Item {i}")
            self.list_widget.addItem(item)

        # Crear un layout y agregar el QListWidget
        layout = QVBoxLayout()
        layout.addWidget(self.list_widget)

        # Crear un widget central y establecer el layout
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
