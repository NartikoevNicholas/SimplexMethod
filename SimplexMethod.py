from copy import deepcopy


class Basic:
    # Создаем объекта
    def __init__(self, str_extremum, str_function, list_odd, list_condition, list_free_e):
        self.dict_results = dict()
        self.str_extremum = str_extremum
        self.list_odds_function = [float(x) for x in str_function.split(";")]
        self.list_condition = list_condition
        self.list_free_element = [float(x) for x in list_free_e]
        self.list_odds_condition = self.getCanonicalViewOddsConditionAndConnectFreeElement(list_odd)

        self.basic = self.getPrimaryBasic()
        self.main_element = self.getMainElement()
        self.row_coefficient = self.getRowCoefficient()
        self.temp_basic = dict()

    # Приводим к каноническому виду члены условий
    def getCanonicalViewOddsConditionAndConnectFreeElement(self, list_odd):
        # конвертируем строки списка в числа списка
        result = list()
        for i in list_odd:
            temp_list = list()
            for j in i.split(";"):
                temp_list.append(float(j))
            result.append(temp_list)

        # этот цикл связано с "<=" и "="
        for index in range(len(result)):
            for i in range(len(self.list_condition)):
                if i == index:
                    if self.list_condition[index] == "<=" or self.list_condition[index] == "=":
                        result[index].append(float(1))
                    else:
                        result[index].append(float(-1))
                else:
                    result[index].append(float(0))

        # этот цикл связано с "=>"
        for _, i in enumerate(self.list_condition):
            if i == "=>":
                for __, j in enumerate(result):
                    if __ == _:
                        j.append(float(1))
                    else:
                        j.append(float(0))

        # Присоединяем свободные элементы
        for i in range(len(self.list_free_element)):
            result[i].append(self.list_free_element[i])
        return result

    # Первичная базисная таблица
    def getPrimaryBasic(self):
        # Начальная базисная таблица, дальше - НБТ
        dict_basic = dict()

        # Заполняем НБТ (X_, R_)
        r = 1
        dict_basic["Basic"] = list()
        for i in range(len(self.list_odds_function) + len(self.list_odds_condition)):
            dict_basic["Basic"].append("X_" + str(i + 1))

        for _, i in enumerate(self.list_odds_condition):
            if self.list_condition[_] == "<=" or self.list_condition[_] == "=":
                dict_basic["X_" + str(_ + len(self.list_odds_function) + 1)] = i
            elif self.list_condition[_] == "=>":
                dict_basic["Basic"].append("R_" + str(r))
                dict_basic["R_" + str(r)] = i
                r += 1

        # Заполняем строку "F" в НБТ
        dict_basic["F"] = list()
        if self.str_extremum == "max":
            for i in self.list_odds_function:
                dict_basic["F"].append(i * (-1))
            for i in range(len(self.list_odds_condition[0]) - len(self.list_odds_function) - 1):
                dict_basic["F"].append(float(0))
            dict_basic["F"].append(float(0))
        else:
            dict_basic["F"] = self.list_odds_function
            for i in range(len(self.list_odds_condition[0]) - len(self.list_odds_function) - 1):
                dict_basic["F"].append(float(0))
            dict_basic["F"].append(float(0))

        # Продолжаем заполняем НБТ (W_)
        w = 1
        for _, i in enumerate(self.list_condition):
            if i == "=>":
                dict_basic["W_" + str(w)] = list()
                for j in self.list_odds_condition[_]:
                    dict_basic["W_" + str(w)].append(j * (-1))
                dict_basic["W_" + str(w)][-2] = float(0)
                w += 1

        # Определяем ведущую строку
        name_row = list(dict_basic.keys())[-1]
        leading_column = dict_basic[name_row].index(min(dict_basic[name_row][0:-1]))

        # Считаем столбец отношений
        dict_basic["Basic"].append("Free element")
        dict_basic["Basic"].append("Attitude")
        for i in dict_basic:
            if i == "Basic":
                continue
            dict_basic[i].append(getAttitude(dict_basic[i][-1], dict_basic[i][leading_column]))

        self.dict_results[0] = dict_basic
        return dict_basic

    # Вторичная базисная таблица
    def getSecondaryBasic(self):
        result = dict()

        # шапка таблицы
        result["Basic"] = self.basic["Basic"]

        # Считаем костяк таблицы
        for _, i in enumerate(self.basic):
            if i == "Basic":
                continue
            if _ == self.main_element[2]:
                str_key = result["Basic"][self.main_element[1]]
                result[str_key] = self.row_coefficient
                continue
            temp_row = list()
            for __, j in enumerate(self.basic[i][0:-1]):
                y = self.row_coefficient[__]
                temp_row.append(j - (y * self.basic[i][self.main_element[1]]))
            result[i] = temp_row

        # Проверяем можем ли удалить псевдофункции (Если таковые есть)
        self.temp_basic = result
        result = self.dropRow()

        # Считаем столбец отношений
        name_row = list(result.keys())[-1]
        leading_column = result[name_row].index(min(result[name_row][0:-1]))
        for i in result:
            if i == "Basic":
                continue
            result[i].append(getAttitude(result[i][-1], result[i][leading_column]))

        self.basic = result

    # Главный элемент и его индексы
    def getMainElement(self):
        # Номер строки и столбца и элемент этого индекса
        result = list()

        # Номер стобца
        name_row = list(self.basic.keys())[-1]
        leading_column = self.basic[name_row].index(min(self.basic[name_row][0:-2]))

        # Номер строки
        str_key = ""
        temp_value = 0
        for i in self.basic:
            if i == "Basic":
                continue
            if self.basic[i][-1] is not None:
                temp_value = self.basic[i][-1]
                str_key = i
                break

        for i in self.basic:
            if i == "Basic":
                continue
            if self.basic[i][-1] is not None and temp_value > self.basic[i][-1]:
                temp_value = self.basic[i][-1]
                str_key = i
        leading_row = list(self.basic.keys()).index(str_key)

        # Добавление элементов
        result.append(self.basic[str_key][leading_column])
        result.append(leading_column)
        result.append(leading_row)
        return result

    # Строка коэффициентов
    def getRowCoefficient(self):
        result = list()
        list_row = self.basic[list(self.basic.keys())[self.main_element[2]]][0:-1]
        if self.main_element[0] == 1:
            return list_row
        for i in list_row:
            result.append(i / self.main_element[0])
        return result

    # Удаление строки
    def dropRow(self):
        result = deepcopy(self.temp_basic)
        value = 0

        # Ищем псевдофункции
        for i in self.temp_basic["Basic"]:
            if i[0] == "R":
                value += 1

        # если value равно ноль значит в таблице нет псевдофункий
        if value == 0:
            return result

        # ищем строки которые нужно дропнуть, если таковые есть
        for i in range(value):
            int_index = self.temp_basic["Basic"].index("R_" + str(i + 1))
            if self.validOnDelFunc(i, int_index):
                for j in self.temp_basic:
                    if j == "Basic":
                        del result[j][int_index]
                        continue
                    if j == "W_" + str(i + 1):
                        del result["W_" + str(i + 1)]
                        continue
                    temp_list = list()
                    for k in range(len(self.temp_basic[j])):
                        if k == int_index:
                            continue
                        temp_list.append(self.temp_basic[j][k])
                    result[j] = temp_list
        return result

    # Проверка для того что бы удалить строку
    def validOnDelFunc(self, index, int_index):
        result = True
        list_odds = self.temp_basic["W_" + str(index + 1)][0:-1]
        for i in range(len(list_odds)):
            if i == int_index:
                if list_odds[i] == 1:
                    continue
                else:
                    result = False
                    break
            if list_odds[i] != 0:
                result = False
                break
        return result

    def getResultDict(self):
        while True:
            if validAttitude(self.basic):
                break
            if validFunction(self.basic["F"][0:-2]):
                break
            self.getSecondaryBasic()
            pass


# Заполяняет столбец "Отношение"
def getAttitude(float_free_element, float_element_main_row):
    result = 0
    if float_free_element <= 0 or float_element_main_row <= 0:
        return None
    result = float_free_element/float_element_main_row
    return result


# Провверка столбца "Отношение" на неопределенные значения
def validAttitude(dict_basic):
    result = True
    for i in dict_basic:
        if i == "Basic":
            continue
        if dict_basic[i][-1] is not None:
            return False
    return result


def validFunction(list_function):
    result = True
    for i in list_function:
        if 0 > i:
            return result
    return False

"""
func = "1;2"
extremum = "max"
odd = ["-1;1", "1;-2", "1;1"]
condition = ["<=", "<=", "<="]
free_e = ["1", "1", "3"]

func = "-1;2"
extremum = "max"
odd = ["1;1", "2;1"]
condition = ["<=", "=>"]
free_e = ["2", "1"]

func = "-6;4;4"     
extremum = "min"
odd = ["-3;-1;1", "-2;-4;1"]
condition = ["<=", "=>"]
free_e = ["2", "3"]

func = "6;3;-1"
extremum = "min"
odd = ["-1;4;2", "5;3;1"]
condition = ["=>", "=>"]
free_e = ["4", "1"]

func = "3;2"
extremum = "max"
odd = ["3;1", "2;-2"]
condition = ["<=", "<="]
free_e = ["2", "-1"]



pb = PrimaryBasic(extremum, func, odd, condition, free_e).primary_basic
while validFunction(pb[list(pb.keys())[-1]][0:-2]):
    if validAttitude(pb):
        print("break")
        break
    pb = SecondaryBasic(pb).secondary_basic
"""