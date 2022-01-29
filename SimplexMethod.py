def getListFloatOdds(str_temp, ex=None):
    try:
        result = list()
        for i in str_temp.split(";"):
            if i == "":
                continue
            result.append(float(i))
        return result
    except ex:
        return ex


def getCanonicalViewCondition(list_odds_condition, list_condition, index):
    result = list_odds_condition
    for i in range(len(list_condition)):
        if i == index:
            if list_condition[index] == "<=" or list_condition[index] == "=":
                result.append(float(1))
            else:
                result.append(float(-1))
        else:
            result.append(float(0))
    return result


def connectFreeElement(list_odds, list_condition, list_free_odds):
    result = list_odds
    for _, i in enumerate(list_condition):
        # это условие связано с r_i, где i = 1,2,3 ...
        if list_condition[_] == "=>":
            for index, j in enumerate(list_odds):
                if index == _:
                    result[index].append(float(1))
                else:
                    result[index].append(float(0))
    for _, i in enumerate(list_free_odds):
        result[_].append(list_free_odds[_])
    return result


# Заполняет строку функции(F) начального базиса (ТОЛЬКО ДЛЯ НАЧАЛЬНОГО БАЗИСА)
def getRowFunction(list_odds_function, int_value, str_extremum, last_element=0):
    result = list()
    if str_extremum == "max":
        for i in list_odds_function:
            result.append(i * (-1))
        for i in range(int_value - len(list_odds_function) - 1):
            result.append(float(0))
        result.append(float(last_element))
    else:
        result = list_odds_function
    return result


# Заполяняет столбец "Отношение"
def getAttitude(float_free_element, float_element_main_row):
    result = 0
    if float_free_element < 0 or float_element_main_row < 0:
        return None
    result = float_free_element/float_element_main_row
    return result


def getDictBasic(str_function, str_extremum, list_str_odds, list_condition, list_str_free_element):
    # Список членов функций при переменных
    list_odds_function = getListFloatOdds(str_function)
    # Список челенов в условиях при переменных
    list_odds_condition = list()
    # Список свободных членов
    list_free_element = list()
    # Основной базис
    dict_basic = dict()

    # Цикл заполняющий "list_free_element" и "list_odds_condition"
    for _, i in enumerate(list_str_odds):
        list_odds_condition.append(getListFloatOdds(i))
        list_free_element.append(float(list_str_free_element[_]))
    # Условие определяющие к чему стримиться фукция
    if str_extremum == "max":
        for _, i in enumerate(list_odds_condition):
            list_odds_condition[_] = getCanonicalViewCondition(i, list_condition, _)
        list_odds_condition = connectFreeElement(list_odds_condition, list_condition, list_free_element)

        r = 1
        for _, i in enumerate(list_odds_condition):
            if list_condition[_] == "<=" or list_condition[_] == "=":
                dict_basic["X_" + str(_ + len(list_odds_function) + 1)] = i
            elif list_condition[_] == "=>":
                dict_basic["R_" + str(r)] = i
                r += 1

        dict_basic["F"] = getRowFunction(list_odds_function, len(list_odds_condition[0]))

        for _, i in enumerate(list_condition):
            if i == "=>":
                temp_row = list()
                for j in list_odds_condition[_]:
                    temp_row.append(j * (-1))
                temp_row[-2] = float(0)
                dict_basic["W_" + str(_ + 1)] = temp_row
    else:
        for _, i in enumerate(list_odds_function):
            list_odds_function[_] = i * (-1)
    leading_column = dict_basic["F"].index(min(dict_basic["F"]))
    for i in dict_basic:
        dict_basic[i.title()].append(getAttitude(dict_basic[i.title()][-1], dict_basic[i.title()][leading_column]))
    return dict_basic


def roleTriangle(past_element_1, past_element_2, past_element_3):
    result = past_element_1 - (past_element_2 * past_element_3)
    return result


def getMainElement(dict_basic):
    result = list()
    list_column = list()
    list_row = list()
    for i in dict_basic["F"]:
        if i is None:
            continue
        list_column.append(i)
    number_column = list_column.index(min(list_column))
    for i in dict_basic:
        if dict_basic[i.title()][-1] is None:
            continue
        list_row.append(dict_basic[i.title()][-1])
    number_row = list_row.index(min(list_row))
    str_key = str()
    for _, i in enumerate(dict_basic):
        if number_row == _:
            str_key = i
    result.append(dict_basic[str_key][number_column])
    result.append(number_row)
    return result


def getNewDictBasic(dict_basic):
    result = dict()
    main_element = getMainElement(dict_basic)
    for _, i in enumerate(dict_basic.values()):
        if _ == main_element[1]:
            pass

"""
func = "1;2"
extremum = "max"
odd = ["-1;1", "1;-2", "1;1"]
condition = ["<=", "=", "<="]
free_e = ["1", "1", "3"]
"""
func = "-1;2"
extremum = "max"
odd = ["1;1", "2;1"]
condition = ["<=", "=>"]
free_e = ["2", "1"]
"""
func = "-6;4;4"
extremum = "min"
odd = ["-3;-1;1", "-2;-4;1"]
condition = ["<=", "=>"]
free_e = ["2", "3"]
"""
basic = getDictBasic(func, extremum, odd, condition, free_e)
#getNewDictBasic(basic)
print(basic)
