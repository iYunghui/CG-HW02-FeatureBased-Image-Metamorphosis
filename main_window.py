"""
main window form file
"""
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow

#from generate_file.ui_main_window import Ui_MainWindow
from generate_file import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Main window form
    """

    def __init__(self, parent=None):
        """Initialize function

        Args:
            parent (QWidget, optional): parent of this form. Defaults to None.
        """
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
