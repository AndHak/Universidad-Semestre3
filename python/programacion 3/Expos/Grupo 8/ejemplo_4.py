import sys
import time
from PySide6.QtCore import QThread, Signal, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QProgressBar, QProgressDialog

class WorkerThread(QThread):
    progress = Signal(int)
    finished = Signal()

    def run(self):
        for i in range(101):
            time.sleep(0.1) 
            self.progress.emit(i)
        self.finished.emit()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Progress Example")
        self.setGeometry(100, 100, 400, 200)

        self.progress_bar = QProgressBar()
        self.progress_bar.setMinimum(0)
        self.progress_bar.setMaximum(100)

        self.button = QPushButton("Start Task")
        self.button.clicked.connect(self.start_task)

        layout = QVBoxLayout()
        layout.addWidget(self.progress_bar)
        layout.addWidget(self.button)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

    def start_task(self):
        self.progress_dialog = QProgressDialog("Processing...", "Cancel", 0, 100, self)
        self.progress_dialog.setWindowTitle("Progress Dialog")
        self.progress_dialog.setWindowModality(Qt.WindowModal)
        self.progress_dialog.setMinimumDuration(50000)
        self.progress_dialog.setValue(0)
        self.progress_dialog.canceled.connect(self.cancel_task)

        self.thread = WorkerThread()
        self.thread.progress.connect(self.update_progress)
        self.thread.finished.connect(self.task_finished)
        self.thread.start()

    def update_progress(self, value):
        self.progress_bar.setValue(value)
        self.progress_dialog.setValue(value)

    def cancel_task(self):
        self.thread.terminate()
        self.progress_dialog.hide()

    def task_finished(self):
        self.progress_dialog.hide()
        self.button.setEnabled(True)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
