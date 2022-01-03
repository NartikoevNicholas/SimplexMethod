import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow


def application():
    app = QApplication(sys.argv)

    windows = QMainWindow()
    windows.setWindowTitle("Simplex method")
    windows.setGeometry(0, 0, 300, 250)
    windows.setBackgroundRole()
    windows.show()
    print("Fdsfd")
    sys.exit(app.exec_())


application()