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
            result.append(0)
    return result


def getQuantityColumnsAndRows(list_condition, str_extremum, int_quantity_odds_function):
    result = list()
    rows = 0
    column = int_quantity_odds_function + len(list_condition)
    if str_extremum == "max":
        for i in list_condition:
            if i == "=>":
                rows += 2
                column += 1
            else:
                rows += 1
    else:
        rows = len(list_condition) * 2
        for i in list_condition:
            column += 1
    result.append(rows + 1)
    result.append(column + 2)
    return result


# поменяй название фукции
def getUntitled(list_odds, list_condition):
    result = list()
    for _, i in enumerate(list_condition):
        pass


def getSolutionSM(str_function, str_extremum, list_str_odds, list_condition, list_str_free_element):
    # Список членов функций при переменных
    list_odds_function = getListFloatOdds(str_function)
    # Список челенов в условиях при переменных
    list_odds_condition = list()
    # Список свободных членов
    list_free_element = list()
    # Основной базис
    dict_condition = dict()
    # Количество столбцов в начальном базисе
    quantityColmnAndRows = getQuantityColumnsAndRows(list_condition, str_extremum, len(list_odds_function))

    # Цикл заполняющий "list_free_element" и "list_odds_condition"
    for _, i in enumerate(list_str_odds):
        list_odds_condition.append(getListFloatOdds(i))
        list_free_element.append(float(list_str_free_element[_]))
    # Условие определяющие к чему стримиться фукция
    if str_extremum == "max":
        for _, i in enumerate(list_odds_condition):
            list_odds_condition[_] = getCanonicalViewCondition(i, list_condition, _)
        print(list_odds_condition)
    else:
        for _, i in enumerate(list_odds_function):
            list_odds_function[_] = i * (-1)


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
getSolutionSM(func, extremum, odd, condition, free_e)
