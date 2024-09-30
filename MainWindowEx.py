from PyQt6.QtWidgets import QApplication, QMessageBox, QLineEdit, QListWidget, QPushButton, QMainWindow
from MainWindow import Ui_MainWindow
import sys

# Cơ sở dữ liệu khách hàng đơn giản (dùng từ điển)
customers = {}


class MainWindowEx(Ui_MainWindow):
    def __init__(self):
        super().__init__()  # Khởi tạo lớp cha
        self.MainWindow = None  # Khởi tạo MainWindow
        self.id_input = None  # Tham chiếu cho id_input
        self.name_input = None  # Tham chiếu cho name_input
        self.email_input = None  # Tham chiếu cho email_input
        self.customer_list = None  # Tham chiếu cho customer_list
        self.add_button = None  # Tham chiếu cho add_button
        self.edit_button = None  # Tham chiếu cho edit_button
        self.delete_button = None  # Tham chiếu cho delete_button
        self.reset_button = None  # Tham chiếu cho reset_button

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
