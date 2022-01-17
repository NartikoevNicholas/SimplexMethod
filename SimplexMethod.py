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
            if list_condition[index] == "<=":
                result.append(float(1))
            else:
                result.append(float(-1))
        else:
            result.append(float(0))
    return result


def connectFreeElement(list_odds, list_condition, list_free_odds):
    result = list_odds
    for _, i in enumerate(list_condition):
        if list_condition[_] == "=>":
            for index, j in enumerate(list_odds):
                if index == _:
                    result[index].append(float(1))
                else:
                    result[index].append(float(0))
    for _, i in enumerate(list_free_odds):
        result[_].append(list_free_odds[_])
    return result


def addRowFunction(list_free_odds, int_value):
    result = list()
    for i in list_free_odds:
        result.append(i * (-1))
    for i in range(int_value - len(list_free_odds)):
        result.append(float(0))
    return result


def getAttitude(float_free_element, float_element_main_row):
    result = 0
    if float_free_element > 0 or float_element_main_row > 0:
        return None
    result =

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
        for _, i in enumerate(list_odds_condition):
            dict_basic["X_" + str(_ + len(list_odds_function) + 1)] = i
        dict_basic["F"] = addRowFunction(list_odds_function, len(list_odds_condition[0]))
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
        print(dict_basic[i.title()][leading_column])
        dict_basic[i.title()].append(2)
    #print(dict_basic)
    return dict_basic



def getNewDictBasic(dict_basic):
    leading_column = dict_basic["F"].index(min(dict_basic["F"]))


func = "1;2"
extremum = "max"
odd = ["-1;1", "1;-2", "1;1"]
condition = ["<=", "<=", "<="]
free_e = ["1", "1", "3"]
"""
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
"""
basic = getDictBasic(func, extremum, odd, condition, free_e)
