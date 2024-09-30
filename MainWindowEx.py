import sys

from PyQt6.QtWidgets import QMessageBox, QApplication

from MainWindow import Ui_MainWindow

customers = {}
class MainWindowEx(Ui_MainWindow):
    def __init__(self):
        pass
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow

        self.add_button.clicked.connect(self.add_customer)
        self.edit_button.clicked.connect(self.edit_customer)
        self.delete_button.clicked.connect(self.delete_customer)
        self.reset_button.clicked.connect(self.reset_fields)
        self.customer_list.itemClicked.connect(self.load_selected_customer)
        self.load_customers()



        # Hien thong tin khach hang
    def load_customers(self):
        self.customer_list.clear()
        for cid, details in customers.items():
            self.customer_list.addItem(f"ID: {cid} | Name: {details['name']} | Email: {details['email']}")

            # ADD CUSTOMER

    def add_customer(self):
        cid = self.id_input.text()
        name = self.name_input.text()
        email = self.email_input.text()

        if cid in customers:
            QMessageBox.critical(self, "Lỗi", "Mã khách hàng đã tồn tại!")
            return

        if not cid or not name or not email:
            QMessageBox.critical(self, "Lỗi", "Vui lòng nhập đầy đủ thông tin!")
            return

        customers[cid] = {'name': name, 'email': email}
        QMessageBox.information(self, "Thành công", "Khách hàng đã được thêm!")
        self.load_customers()

        # Xóa khách hàng
    def delete_customer(self):
        cid = self.id_input.text()

        if cid not in customers:
            QMessageBox.critical(self, "Lỗi", "Không tìm thấy mã khách hàng!")
            return

        del customers[cid]
        QMessageBox.information(self, "Thành công", "Khách hàng đã được xóa!")
        self.load_customers()

        # Xóa các trường nhập liệu
    def reset_fields(self):
        self.id_input.clear()
        self.name_input.clear()
        self.email_input.clear()

            # EDIT CUSTOMER
    def edit_customer(self):
        cid = self.id_input.text()

        if cid not in customers:
            QMessageBox.critical(self, "Lỗi", "Không tìm thấy mã khách hàng!")
            return

        name = self.name_input.text()
        email = self.email_input.text()

        if not name or not email:
            QMessageBox.critical(self, "Lỗi", "Vui lòng nhập đầy đủ thông tin!")
            return

        customers[cid]['name'] = name
        customers[cid]['email'] = email
        QMessageBox.information(self, "Thành công", "Thông tin khách hàng đã được cập nhật!")
        self.load_customers()

        # UPDATE IN4 CUSTOMER
    def load_selected_customer(self):
        selected = self.customer_list.currentItem().text()
        cid = selected.split('|')[0].split(':')[1]

        customer = customers[cid]
        self.id_input.setText(cid)
        self.name_input.setText(customer['name'])
        self.email_input.setText(customer['email'])

    def show(self):
        self.MainWindow.show()
