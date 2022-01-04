def convertStringToNumber(str_temp, ex=None):
    try:
        number = float(str_temp)
        return number
    except ex:
        return ex


def getOddsFunction(str_function, str_extremum, ex=None):
    try:
        list_odds = str_function.split(";")
        temp_list = list()
        if str_extremum == "max":
            for index, i in enumerate(list_odds):
                if list_odds[index] == "":
                    break
                temp_list.append(convertStringToNumber(list_odds[index]))
            return temp_list
        else:
            for index, i in enumerate(list_odds):
                if list_odds[index] == "":
                    break
                temp_list.append(convertStringToNumber(list_odds[index]) * (-1))
            return temp_list
    except ex:
        return ex


def getOddsCondition(odds, free_el, list_condition, ex=None):
    try:
        result = list()
        list_odds = list()
        list_free_el = list()
        for i in odds:
            list_temp_odds = list()
            for j in i.split(";"):
                list_temp_odds.append(convertStringToNumber(j))
            list_odds.append(list_temp_odds)
        for i in free_el:
            list_temp_free_el = list()
            for j in i.split(";"):
                list_temp_free_el.append(convertStringToNumber(j))
            list_free_el.append(list_temp_free_el)
        result.append(list_odds)
        result.append(list_free_el)
        return result
    except ex:
        return ex


def getOddsCondition1(odds, free_el, list_condition, ex=None):
    try:
        result = list()
        for index, i in enumerate(list_condition):
            if i == "<=":
                pass




        list_odds = list()
        list_free_el = list()
        for i in odds:
            list_temp_odds = list()
            for j in i.split(";"):
                list_temp_odds.append(convertStringToNumber(j))
            list_odds.append(list_temp_odds)
        for i in free_el:
            list_temp_free_el = list()
            for j in i.split(";"):
                list_temp_free_el.append(convertStringToNumber(j))
            list_free_el.append(list_temp_free_el)
        result.append(list_odds)
        result.append(list_free_el)
        return result
    except ex:
        return ex


def getBasicTableOne(list_function_odds, list_odds_condition, list_condition, ex=None):
    try:    
        result = list()
        odds_condition = list_odds_condition[0]
        for index, i in enumerate(odds_condition):
            temp_list = list()
            temp_odds = odds_condition[index]
            for _, j in enumerate(temp_odds):
                temp_list.append(temp_odds[_])
            temp_list.append(1 if list_condition[index] == "<=" else -1)
            result.append(temp_list)
        return result
    except ex:
        return ex


def getSolutionSM(str_function, str_extremum, list_str_odds, list_condition, list_free_element):
    list_odds_function = getOddsFunction(str_function, str_extremum)
    if str_extremum == "max":
        pass
#       list_odds_condition = getOddsCondition1(list_str_odds,list_free_element,list_condition)
    else:
        pass
    pass


func = "-1;2"
extremum = "max"
odd = ["-1;1", "1;-2", "1;1"]
condition = ["<=", "<=", "<="]
free_e = ["1", "1", "3"]
getSolutionSM(func,extremum,odd,condition,free_e)
