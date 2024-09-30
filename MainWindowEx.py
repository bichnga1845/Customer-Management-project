from MainWindow import Ui_MainWindow


class MainWindowEx(Ui_MainWindow):
    customers = {}
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

        self.MainWindow=MainWindow
    def show(self):
        self.MainWindow.show()