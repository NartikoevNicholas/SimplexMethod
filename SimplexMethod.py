def getFunctionData(str_function, str_extremum, ex=None):
    try:
        list_odds = str_function.split(";")
        temp_list = list()
        if str_extremum == "max":
            for index, i in enumerate(list_odds):
                if list_odds[index] == "":
                    break
                temp_list.append(float(list_odds[index]))
            return temp_list
        else:
            for index, i in enumerate(list_odds):
                if list_odds[index] == "":
                    break
                temp_list.append(float(list_odds[index]) * (-1))
            return temp_list
    except ex:
        return ex


print(getFunctionData("-3.3;1.1;-2;4.3", "min"))
print(getFunctionData("-6;2;6", "max"))
