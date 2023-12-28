from PyQt6.QtWidgets import QWidget, QPushButton, QMessageBox, QTableWidgetItem
from system_window import Ui_Form
from connect_db import ConnectDatabase


class SystemWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.db = ConnectDatabase()
        self.student_id = self.ui.lineEdit_no
        self.first_name = self.ui.lineEdit_isim
        self.last_name = self.ui.lineEdit_soyisim
        self.email_address = self.ui.lineEdit_eposta
        self.parent_name = self.ui.lineEdit_veli
        self.closeness = self.ui.lineEdit_yakinlik
        self.tel1 = self.ui.lineEdit_tel1
        self.tel2 = self.ui.lineEdit_tel2
        self.birth_date = self.ui.dateEdit
        self.adres = self.ui.textEdit_adres

        self.add_btn = self.ui.pushButton_ekle
        self.update_btn = self.ui.pushButton_guncelle
        self.select_btn = self.ui.pushButton_sec
        self.search_btn = self.ui.pushButton_ara
        self.clear_btn = self.ui.pushButton_temizle
        self.delete_btn = self.ui.pushButton_sil

        self.result_table = self.ui.tableWidget
        self.button_list = self.ui.func_frame.findChildren(QPushButton)
        self.init_signal_slot()
        self.search_info()

    def init_signal_slot(self):
        self.add_btn.clicked.connect(self.add_info)
        self.update_btn.clicked.connect(self.update_info)
        self.delete_btn.clicked.connect(self.delete_info)
        self.select_btn.clicked.connect(self.select_info)
        self.clear_btn.clicked.connect(self.clear_info)
        self.search_btn.clicked.connect(self.search_info)

    def add_info(self):
        # Function to add student information
        self.disable_buttons()

        student_info = self.get_student_info()

        if student_info["student_id"] and student_info["first_name"]:
            check_result = self.check_student_id(student_id=int(student_info["student_id"]))

            if check_result:
                QMessageBox.information(self, "Warning", "Please input a new student ID",
                                        QMessageBox.StandardButton.Ok)
                self.enable_buttons()
                return
            add_result = None
            try:
                add_result = self.db.add_info(student_info)
                print("Kayıt başarıyla eklendi.")
            except Exception as e:
                QMessageBox.information(self, "Warning", f"Add fail: {add_result}, Please try again.",
                                        QMessageBox.StandardButton.Ok)

        else:
            QMessageBox.information(self, "Warning", "Please input student ID and first name.",
                                    QMessageBox.StandardButton.Ok)

        self.search_info()
        self.enable_buttons()

    def update_info(self):
        pass

    def delete_info(self):
        pass

    def select_info(self):
        pass

    def clear_info(self):
        pass

    def search_info(self):
        student_info = self.get_student_info()
        search_result = self.db.search_info(student_info)
        self.show_data(search_result)

    def disable_buttons(self):

        for button in self.button_list:
            button.setDisabled(True)

    def enable_buttons(self):

        for button in self.button_list:
            button.setDisabled(False)

    def get_student_info(self):
        student_id = self.student_id.text().strip()
        first_name = self.first_name.text().strip()
        last_name = self.last_name.text().strip()
        email_address = self.email_address.text().strip()
        tel1 = self.tel1.text().strip()
        tel2 = self.tel2.text().strip()
        parent_name = self.parent_name.text().strip()
        closeness = self.closeness.text().strip()
        adres = self.adres.toPlainText().strip()
        birth_date = self.birth_date.date()
        day = birth_date.day()
        month = birth_date.month()
        year = birth_date.year()
        iso_date = f"{year:04d}-{month:02d}-{day:02d}T00:00:00Z"

        student_info = {
            "student_id": student_id,
            'first_name': first_name,
            'last_name': last_name,
            'email': email_address,
            'tel1': tel1,
            'tel2': tel2,
            'parent_name': parent_name,
            'closeness': closeness,
            'birth_date': iso_date,
            'adres': adres
        }

        return student_info

    def check_student_id(self, student_id):
        result = self.db.get_single_data(student_id)
        return result

    def show_data(self, result):
        # Function to populate the table with student information
        if result:
            self.result_table.setRowCount(0)
            self.result_table.setRowCount(len(result))

            for row, info in enumerate(result):
                info_list = [
                    info["student_id"],
                    info["first_name"],
                    info["last_name"],
                    info["parent_name"],
                    info["closeness"],
                    info["birth_date"],
                    info["tel1"],
                    info["tel2"],
                    info["email"],
                    info["adres"]
                ]

                for column, item in enumerate(info_list):
                    cell_item = QTableWidgetItem(str(item))
                    self.result_table.setItem(row, column, cell_item)

        else:
            self.result_table.setRowCount(0)
            return

