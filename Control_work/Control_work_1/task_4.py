"""
На вход функции подается строка.
Функция должна вернуть слово, которое в этой строке встречается чаще всего.
Если таких слов несколько, пусть функция вернет 0.

Примеры:
Вход 1: apple orange banana banana orange banana
Выход 1: banana

Вход 2: apple orange banana orange banana
Выход 2: 0
"""


def most_frequent_word(string):
    lst = string.split()
    dct = {}
    for item in lst:
        if item not in dct:
            dct[item] = 1
        else:
            dct[item] += 1
    max_count = 0
    word = ""
    for key, value in dct.items():
        if value > max_count:
            max_count = value
            word = key
        elif value == max_count:
            word = 0
    return word


def most_frequent_word_2(string):
    lst = string.split()
    max_count = 0
    word = ""
    for item in lst:
        temp_count = string.count(item)
        if temp_count > max_count:
            max_count = temp_count
            word = item
        elif temp_count == max_count:
            word = 0
    return word


assert most_frequent_word("apple orange banana banana orange banana") == "banana"
assert most_frequent_word("apple orange banana orange banana") == 0
