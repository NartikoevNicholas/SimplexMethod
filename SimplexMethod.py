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


def getRowMax(list_odd_condition, str_condition):
    result = list_odd_condition
    if str_condition == "<=":
        result.append(float(1))
    else:
        result.append(float(-1))
    return result


def getSolutionSM(str_function, str_extremum, list_str_odds, list_condition, list_str_free_element):

    # Список членов функций при переменных
    list_odds_function = getListFloatOdds(str_function)
    # Список челенов в условиях при переменных
    list_odds_condition = list()
    # Список свободных членов
    list_free_element = list()
    # Основной базис
    dict_condition = dict()

    # Цикл заполняющий "list_free_element" и "list_odds_condition"
    for _, i in enumerate(list_str_odds):
        list_odds_condition.append(getListFloatOdds(i))
        list_free_element.append(float(list_str_free_element[_]))

    # Условие определяющие к чему стримиться фукция
    if str_extremum == "max":
        for _, i in enumerate(list_odds_condition):
            list_odds_condition[_] = getRowMax(i, list_condition[_])
    else:
        for _, i in enumerate(list_odds_function):
            list_odds_function[_] = i * (-1)
    pass
    print(list_odds_function)


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
