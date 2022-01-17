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





func = "-1;2"
extremum = "max"
odd = ["-1;1", "1;-2", "1;1"]
condition = ["<=", "<=", "<="]
free_e = ["1", "1", "3"]
getSolutionSM(func, extremum, odd, condition, free_e)
