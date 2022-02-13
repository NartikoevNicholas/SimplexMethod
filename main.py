import sys
from ViewApp import MainWindow
from PyQt5.QtWidgets import QApplication


app = QApplication(sys.argv)
win = MainWindow()
win.main_window.show()
sys.exit(app.exec_())
