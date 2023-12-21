from PyQt6.QtWidgets import QWidget
from system_window import Ui_Form


class SystemWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

