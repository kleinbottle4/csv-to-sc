def is_subset(array1, array2):
    for elem in array1:
        if not elem in array2:
            return False
    return True

def is_float(string):
    if string == '':
        return False
    elif not is_subset(string, "0123456789.e"):
        return False
    else:
        num_of_es = string.count('e')
        if num_of_es > 1:
            return False
        elif num_of_es == 1:
            sci = string.split('e')
            if not is_subset(sci[0] + sci[1], "0123456789."):
                return False
        elif string.count('.') > 1:
            return False
        else:
            return True

def is_int(string):
    return string != '' and is_subset(string, "0123456789")

def table_to_nums(table):
    for i, array in enumerate(table):
        for j, string in enumerate(array):
            if is_int(string):
                table[i][j] = int(string)
            elif is_float(string):
                table[i][j] = float(string)
    return table

def num_to_sc_col(num):
    assert num <= 701, "SC columns only go up to ZZ"
    num = int(num)
    ALPHABET = "abcdefghijklmnopqrstuvwxyz"
    if num < 26:
        return ALPHABET[num]
    else:
        second = num % 26
        num -= second
        first = ((num % 676) // 26) - 1 #26 * 26 = 676
        return ALPHABET[first] + ALPHABET[second]
