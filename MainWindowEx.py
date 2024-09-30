from PyQt6.QtWidgets import QApplication, QMessageBox, QLineEdit, QListWidget, QPushButton, QMainWindow
from MainWindow import Ui_MainWindow
import sys

# Cơ sở dữ liệu khách hàng đơn giản (dùng từ điển)
customers = {}


class MainWindowEx(Ui_MainWindow):
    def __init__(self):
        super().__init__()  # Khởi tạo lớp cha


    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
