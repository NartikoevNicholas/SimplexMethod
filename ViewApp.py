from PyQt5 import QtCore, QtGui, QtWidgets


class MainWindow:
    def __init__(self):
        self.main_window = QtWidgets.QMainWindow()
        self.central_widget = QtWidgets.QWidget(self.main_window)
        self.btn_create_condition = QtWidgets.QPushButton(self.central_widget)
        self.label_conditions = QtWidgets.QLabel(self.central_widget)
        self.Extremum = QtWidgets.QComboBox(self.central_widget)
        self.label_arrow = QtWidgets.QLabel(self.central_widget)
        self.line = QtWidgets.QFrame(self.central_widget)
        self.label_Function = QtWidgets.QLabel(self.central_widget)
        self.function_odds = QtWidgets.QLineEdit(self.central_widget)
        self.list_condition = list()
        self.ElementWindow()

    def ElementWindow(self):
        self.main_window.setObjectName("MainWindow")
        self.main_window.resize(500, 400)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.main_window.setFont(font)
        self.main_window.setStyleSheet("background-color: rgb(248, 255, 171);")

        self.central_widget.setObjectName("central_widget")

        # надпись "Function"
        self.label_Function.setGeometry(QtCore.QRect(30, 10, 91, 21))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label_Function.setFont(font)
        self.label_Function.setStyleSheet("")
        self.label_Function.setTextFormat(QtCore.Qt.AutoText)
        self.label_Function.setObjectName("label_Function")
        self.label_Function.setText("Function")

        # Поле ввода членов
        self.function_odds.setGeometry(QtCore.QRect(125, 13, 241, 21))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(12)
        self.function_odds.setFont(font)
        self.function_odds.setStyleSheet("color: rgb(0, 0, 0);\n"
                                         "background-color: rgb(255, 255, 255);")
        self.function_odds.setObjectName("function_odds")

        # Горизонтальная черта
        self.line.setGeometry(QtCore.QRect(10, 40, 480, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        # Стрелка
        self.label_arrow.setGeometry(QtCore.QRect(370, 13, 31, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_arrow.setFont(font)
        self.label_arrow.setText("")
        self.label_arrow.setPixmap(QtGui.QPixmap("right.ico"))
        self.label_arrow.setObjectName("label")

        # Экстремум
        self.Extremum.setGeometry(QtCore.QRect(405, 13, 61, 21))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Extremum.setFont(font)
        self.Extremum.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 178, 102, 255), stop:0.55 rgba(235, 148, 61, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));\n"
            "color: rgb(255, 248, 249);")
        self.Extremum.setObjectName("Extremum")
        self.Extremum.addItem("max")
        self.Extremum.addItem("min")


        # Надпись "Add condition"
        self.label_conditions.setGeometry(QtCore.QRect(30, 60, 151, 16))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(16)
        self.label_conditions.setFont(font)
        self.label_conditions.setObjectName("label_conditions")
        self.label_conditions.setText("Add condition")

        # Кнопка добавления условия
        self.btn_create_condition.setGeometry(QtCore.QRect(180, 60, 51, 21))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btn_create_condition.setFont(font)
        self.btn_create_condition.setStyleSheet("background-color: rgb(12, 255, 0);\n"
                                                "color: rgb(255, 255, 255);")
        self.btn_create_condition.setObjectName("btn_create_condition")
        self.btn_create_condition.setText("+")
        self.btn_create_condition.clicked.connect(self.click_btn_create_condition)

        self.main_window.setCentralWidget(self.central_widget)
        QtCore.QMetaObject.connectSlotsByName(self.main_window)

    def click_btn_create_condition(self):
        row = RowCondition(self)
        self.list_condition.append(row)


class RowCondition:
    def __init__(self, main_window):
        self.main_window = main_window
        self.index = len(self.main_window.list_condition)
        self.label_condition = QtWidgets.QLabel(self.main_window.central_widget)
        self.condition_odds = QtWidgets.QLineEdit(self.main_window.central_widget)
        self.condition = QtWidgets.QComboBox(self.main_window.central_widget)
        self.free_element = QtWidgets.QLineEdit(self.main_window.central_widget)
        self.btn_del_row = QtWidgets.QPushButton(self.main_window.central_widget)
        self.ElementRow()

    def ElementRow(self):
        # Надпись "Odd condition"
        self.label_condition.setGeometry(QtCore.QRect(10, 90 + (30 * len(self.main_window.list_condition)), 150, 21))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_condition.setFont(font)
        self.label_condition.setStyleSheet("")
        self.label_condition.setTextFormat(QtCore.Qt.AutoText)
        self.label_condition.setText("Odds condition")
        self.label_condition.show()

        # Поле ввода членов условий
        self.condition_odds.setGeometry(QtCore.QRect(150, 90 + (30 * len(self.main_window.list_condition)), 150, 21))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(12)
        self.condition_odds.setFont(font)
        self.condition_odds.setStyleSheet("color: rgb(0, 0, 0);\n"
                                         "background-color: rgb(255, 255, 255);")
        self.condition_odds.setObjectName("function_odds")
        self.condition_odds.show()

        # условие
        self.condition.setGeometry(QtCore.QRect(305, 90 + (30 * len(self.main_window.list_condition)), 50, 21))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.condition.setFont(font)
        self.condition.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 178, 102, 255), stop:0.55 rgba(235, 148, 61, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));\n"
            "color: rgb(255, 248, 249);")
        self.condition.setObjectName("Extremum")
        self.condition.addItem("?")
        self.condition.addItem("<=")
        self.condition.addItem("=")
        self.condition.addItem("=>")
        self.condition.show()

        # Поле ввода свободного члена
        self.free_element.setGeometry(QtCore.QRect(360, 90 + (30 * len(self.main_window.list_condition)), 50, 21))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(12)
        self.free_element.setFont(font)
        self.free_element.setStyleSheet("color: rgb(0, 0, 0);\n"
                                          "background-color: rgb(255, 255, 255);")
        self.free_element.setObjectName("function_odds")
        self.free_element.show()

        # Кнопка удаления строки
        self.btn_del_row.setGeometry(QtCore.QRect(415, 90 + (30 * len(self.main_window.list_condition)), 70, 21))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_del_row.setFont(font)
        self.btn_del_row.setStyleSheet("background-color: rgb(255, 0, 0);\n"
                                                "color: rgb(255, 255, 255);")
        self.btn_del_row.setText("Delete")
        self.btn_del_row.clicked.connect(self.click_btn_del_row)
        self.btn_del_row.show()

    def click_btn_del_row(self):
        self.label_condition.deleteLater()
        self.condition_odds.deleteLater()
        self.condition.deleteLater()
        self.free_element.deleteLater()
        self.btn_del_row.deleteLater()
        del self.main_window.list_condition[self.index]