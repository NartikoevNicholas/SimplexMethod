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


def getRow(list_odd_condition, str_condition, float_free_element):
    result = list()
    if str_condition == "<=":
        pass
    else:
        pass

    return result


def getSolutionSM(str_function, str_extremum, list_str_odds, list_condition, list_str_free_element):
    list_odds_function = getListFloatOdds(str_function)
    list_free_element = list()
    list_odds_condition = list()
    for _, i in enumerate(list_str_odds):
        list_odds_condition.append(getListFloatOdds(i))
        list_free_element.append(list_str_free_element[_])
    if str_extremum == "max":
        dict_condition = dict()
        for _, i in enumerate(list_condition):
            dict_condition[_] = getRow(list_odds_condition[_], i, list_free_element[_])
        print(dict_condition)
    else:
        pass
    pass


func = "-1;2"
extremum = "max"
odd = ["-1;1", "1;-2", "1;1"]
condition = ["<=", "<=", "<="]
free_e = ["1", "1", "3"]
getSolutionSM(func, extremum, odd, condition, free_e)
