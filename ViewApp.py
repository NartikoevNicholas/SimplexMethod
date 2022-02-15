from PyQt5 import QtCore, QtGui, QtWidgets
from SimplexMethod import Basic


class MainWindow:
    def __init__(self):
        self.main_window = QtWidgets.QMainWindow()
        self.central_widget = QtWidgets.QWidget(self.main_window)

        self.label_Function = QtWidgets.QLabel(self.central_widget)
        self.function_odds = QtWidgets.QLineEdit(self.central_widget)
        self.label_arrow = QtWidgets.QLabel(self.central_widget)
        self.extremum = QtWidgets.QComboBox(self.central_widget)

        self.line = QtWidgets.QFrame(self.central_widget)
        self.btn_create_condition = QtWidgets.QPushButton(self.central_widget)
        self.check_box = QtWidgets.QCheckBox(self.central_widget)

        self.index = 0
        self.dict_condition = dict()

        self.btn_calculate = QtWidgets.QPushButton(self.central_widget)

        self.dict_basic_table = dict()
        self.btn_to_input = QtWidgets.QPushButton(self.main_window)

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
        self.label_Function.setTextFormat(QtCore.Qt.AutoText)
        self.label_Function.setText("Function")

        # Поле ввода членов
        self.function_odds.setGeometry(QtCore.QRect(125, 13, 241, 21))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(12)
        self.function_odds.setFont(font)
        self.function_odds.setStyleSheet("color: rgb(0, 0, 0);\n"
                                         "background-color: rgb(255, 255, 255);")

        # Горизонтальная черта
        self.line.setGeometry(QtCore.QRect(10, 40, 480, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)

        # Стрелка
        self.label_arrow.setGeometry(QtCore.QRect(370, 13, 31, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_arrow.setFont(font)
        self.label_arrow.setText("")
        self.label_arrow.setPixmap(QtGui.QPixmap("right.ico"))

        # Экстремум
        self.extremum.setGeometry(QtCore.QRect(405, 13, 61, 21))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.extremum.setFont(font)
        self.extremum.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 178, 102, 255), stop:0.55 rgba(235, 148, 61, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));\n"
            "color: rgb(255, 248, 249);")
        self.extremum.addItem("max")
        self.extremum.addItem("min")

        # Кнопка добавления условия
        self.btn_create_condition.setGeometry(QtCore.QRect(30, 60, 130, 21))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_create_condition.setFont(font)
        self.btn_create_condition.setStyleSheet("background-color: rgb(12, 255, 0);\n"
                                                "color: rgb(255, 255, 255);")
        self.btn_create_condition.setText("Add condition")
        self.btn_create_condition.clicked.connect(self.click_btn_create_condition)

        # чекбокс
        self.check_box.setGeometry(QtCore.QRect(250, 60, 180, 21))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.check_box.setFont(font)
        self.check_box.setText("Show all basic-table")

        # Кнопка рассчитать
        self.btn_calculate.setGeometry(QtCore.QRect(350, 90, 100, 21))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_calculate.setFont(font)
        self.btn_calculate.setStyleSheet("background-color: rgb(56, 68, 70);\n"
                                                "color: rgb(255, 255, 255);")
        self.btn_calculate.setText("Calculate")
        self.btn_calculate.clicked.connect(self.click_btn_calculate)

        self.btn_to_input.setGeometry(QtCore.QRect(10, 10, 80, 21))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_to_input.setFont(font)
        self.btn_to_input.setStyleSheet("background-color: rgb(56, 68, 70);\n"
                                         "color: rgb(255, 255, 255);")
        self.btn_to_input.setText("To input")
        self.btn_to_input.clicked.connect(self.click_btn_to_input)
        self.btn_to_input.hide()

        self.main_window.setCentralWidget(self.central_widget)
        QtCore.QMetaObject.connectSlotsByName(self.main_window)

    def ShowTable(self):
        self.main_window.centralWidget().hide()
        self.btn_to_input.show()

        if self.check_box.isChecked():
            t = Table(self.main_window, self.dict_basic_table[0])
            t.show()
        else:
            pass
        print()

    def click_btn_create_condition(self):
        for i in range(len(self.dict_condition) + 1):
            if len(self.dict_condition) == 0:
                self.index = 0
                break
            elif self.dict_condition.__contains__(i):
                continue
            else:
                self.index = i
                break
        self.dict_condition[self.index] = RowCondition(self)

    def click_btn_calculate(self):

        # Сбор данных
        extremum = self.extremum.currentText()
        function_odds = self.function_odds.text()
        list_condition_odds = list()
        list_conditions = list()
        list_free_odds = list()
        for i in range(len(self.dict_condition)):
            list_condition_odds.append(self.dict_condition[i].condition_odds.text())
            list_conditions.append(self.dict_condition[i].condition.currentText())
            list_free_odds.append(self.dict_condition[i].free_element.text())

        # Рассчет полученных данных
        try:
            # Симплекс таблицы
            basic = Basic(extremum, function_odds, list_condition_odds, list_conditions, list_free_odds)
            basic.getResultDict()

            # Преобразование данных
            for i in range(len(basic.dict_results)):
                temp_list_table = list()
                list_keys = basic.dict_results[i].keys()
                for key in list_keys:
                    temp_list_row = list()
                    temp_list_row.append(key)
                    list_value_row = basic.dict_results[i][key]
                    for value in list_value_row:
                        temp_list_row.append(str(value))
                    temp_list_table.append(temp_list_row)
                self.dict_basic_table[i] = temp_list_table
            self.ShowTable()

        except Exception as ex:
            print(ex)

    def click_btn_to_input(self):
        self.btn_to_input.hide()
        self.main_window.centralWidget().show()


class RowCondition:
    def __init__(self, main_window):
        self.main_window = main_window
        self.index = self.main_window.index
        self.label_condition = QtWidgets.QLabel(self.main_window.central_widget)
        self.condition_odds = QtWidgets.QLineEdit(self.main_window.central_widget)
        self.condition = QtWidgets.QComboBox(self.main_window.central_widget)
        self.free_element = QtWidgets.QLineEdit(self.main_window.central_widget)
        self.btn_del_row = QtWidgets.QPushButton(self.main_window.central_widget)
        self.ElementRow()

    def ElementRow(self):

        # Отступ
        indent = 90 + (30 * self.index)

        # Надпись "Odd condition"
        self.label_condition.setGeometry(QtCore.QRect(10, indent, 150, 21))
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
        self.condition_odds.setGeometry(QtCore.QRect(150, indent, 150, 21))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(12)
        self.condition_odds.setFont(font)
        self.condition_odds.setStyleSheet("color: rgb(0, 0, 0);\n"
                                         "background-color: rgb(255, 255, 255);")
        self.condition_odds.setObjectName("function_odds")
        self.condition_odds.show()

        # условие
        self.condition.setGeometry(QtCore.QRect(305, indent, 50, 21))
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
        self.free_element.setGeometry(QtCore.QRect(360, indent, 50, 21))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(12)
        self.free_element.setFont(font)
        self.free_element.setStyleSheet("color: rgb(0, 0, 0);\n"
                                          "background-color: rgb(255, 255, 255);")
        self.free_element.setObjectName("function_odds")
        self.free_element.show()

        # Кнопка удаления строки
        self.btn_del_row.setGeometry(QtCore.QRect(415, indent, 70, 21))
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

        # Отступ кнопки "self.main_window.dict_condition"
        if len(self.main_window.dict_condition) == 0:
            self.main_window.btn_calculate.move(350, 120)
        else:
            len_dict = len(self.main_window.dict_condition)
            sup_dict = max(self.main_window.dict_condition.keys())
            if len_dict > sup_dict:
                self.main_window.btn_calculate.move(350, 120 + (30 * len_dict))
            else:
                self.main_window.btn_calculate.move(350, 120 + (30 * sup_dict))

    def click_btn_del_row(self):
        self.label_condition.deleteLater()
        self.condition_odds.deleteLater()
        self.condition.deleteLater()
        self.free_element.deleteLater()
        self.btn_del_row.deleteLater()
        self.main_window.dict_condition.pop(self.index)
        if len(self.main_window.dict_condition) == 0:
            self.main_window.btn_calculate.move(350, 90)
        else:
            self.main_window.btn_calculate.move(350, 120 + (30 * max(self.main_window.dict_condition.keys())))


class Table:
    def __init__(self, main_window, table_list):
        self.main_window = main_window
        self.list_label = list()
        self.getTable(table_list)

    def getTable(self, table_list):
        # Шрифт
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)

        for _, row in enumerate(table_list):
            location_y = 35 + (round(self.main_window.height() / len(table_list)) * _)
            for __, text in enumerate(row):
                location_x = 5 + (round(self.main_window.width() / len(row)) * __)
                label_cell = QtWidgets.QLabel(self.main_window)
                label_cell.setFont(font)
                label_cell.move(location_x, location_y)
                label_cell.adjustSize()
                label_cell.setText(text)
                label_cell.hide()
                self.list_label.append(label_cell)

    def show(self):
        for label in self.list_label:
            label.show()

    def hide(self):
        for label in self.list_label:
            label.hide()