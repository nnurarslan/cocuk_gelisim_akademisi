import sys
from PyQt6.QtWidgets import QApplication, QWidget, QMessageBox, QLineEdit
from login import Ui_Form_login


class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.login_btn = None
        self.show_password_checkbox = None
        self.password = None
        self.username = None
        self.ui_login = None
        self.init_ui()

    def init_ui(self):
        self.ui_login = Ui_Form_login()
        self.ui_login.setupUi(self)
        self.username = self.ui_login.lineEdit_username
        self.password = self.ui_login.lineEdit_password
        self.login_btn = self.ui_login.pushButton_login
        self.show_password_checkbox = self.ui_login.cb_show_pwd
        self.login_btn.clicked.connect(self.login)
        self.password.returnPressed.connect(self.login)
        self.show_password_checkbox.stateChanged.connect(self.toggle_pwd_visibility)

    def login(self):
        if self.username.text() == 'admin' and self.password.text() == '123':
            QMessageBox.information(self, 'Başarılı', 'Giriş Başarılı')
        else:
            QMessageBox.information(self, 'Başarısız', 'Giriş Başarısız')

    def toggle_pwd_visibility(self):
        if self.show_password_checkbox.isChecked() == 1:
            self.password.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self.password.setEchoMode(QLineEdit.EchoMode.Password)


# App entry point
if __name__ == '__main__':
    app = QApplication(sys.argv)
    w_login = LoginWindow()
    w_login.show()
    app.exec()
