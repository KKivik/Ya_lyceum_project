import io
import os
import sys

from PyQt6 import uic  # Импортируем uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog

class Main_w(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('const/Main_selecter.ui', self)  # Загружаем дизайн
        self.pushButton.clicked.connect(self.codec)

    def codec(self):
        self.crypto_form = Cryptographer_window(self)
        self.crypto_form.show()


class Cryptographer_window(QWidget):
    def __init__(self, *args):
        super().__init__()
        uic.loadUi('const/crypter.ui', self)  # Загружаем дизайн
        self.select_folder.clicked.connect(self.selecting_folder)

    def selecting_folder(self):
        fname = QFileDialog.getExistingDirectory(self, 'Выбрать картинку', '')






if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main_w()
    ex.show()
    sys.exit(app.exec())

