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


def getOddsCondition(odds, free_el, ex=None):
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


func = getOddsFunction("1;2", "max")
odd = ["1;1", "1;-2", "1;1"]
#cond = ["<=", "<=", "<="]
free_e = ["1", "1", "3"]
cond = getOddsCondition(odd, free_e)
print(cond)
