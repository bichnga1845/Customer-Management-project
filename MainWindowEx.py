from PyQt6.QtWidgets import QMessageBox

from MainWindow import Ui_MainWindow

customers = {}
class MainWindowEx(Ui_MainWindow):
    def __init__(self):
        pass
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.add_button.clicked.connect(self.add_customer)
        self.edit_button.clicked.connect(self.edit_customer)
        self.delete_button.clicked.connect(self.delete_customer)
        self.reset_button.clicked.connect(self.reset_fields)
        self.customer_list.itemClicked.connect(self.load_selected_customer)
        self.load_customers()
            #Hien thong tin khach hang
        def load_customers(self):
            self.customer_list.clear()
            for id, details in customers.items():
                self.customer_list.addItem(f"ID: {id} | Name: {details['name']} | Email: {details['email']}")

            # ADD CUSTOMER

        def add_customer(self):
            id = self.id_input.text().strip()
            name = self.name_input.text().strip()
            email = self.email_input.text().strip()

            if id in customers:
                QMessageBox.critical(self, "Lỗi", "Mã khách hàng đã tồn tại!")
                return

            if not id or not name or not email:
                QMessageBox.critical(self, "Lỗi", "Vui lòng nhập đầy đủ thông tin!")
                return

            customers[id] = {'name': name, 'email': email}
            QMessageBox.information(self, "Thành công", "Khách hàng đã được thêm!")
            self.load_customers()

        self.MainWindow=MainWindow
    def show(self):
        self.MainWindow.show()