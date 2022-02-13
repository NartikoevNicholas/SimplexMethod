import sys
from ViewApp import MainWindow
from PyQt5.QtWidgets import QApplication


app = QApplication(sys.argv)
win = MainWindow()
win.main_window.show()
sys.exit(app.exec_())


'''
func = "1;2"
extremum = "max"
odd = ["-1;1", "1;-2", "1;1"]
condition = ["<=", "<=", "<="]
free_e = ["1", "1", "3"]
'''