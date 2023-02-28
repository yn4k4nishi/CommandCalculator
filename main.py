import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from ui.calculator import Ui_MainWindow

class CommandCalculator(QMainWindow):
    def __init__(self, parent=None):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    win = CommandCalculator()

    sys.exit(app.exec_())
