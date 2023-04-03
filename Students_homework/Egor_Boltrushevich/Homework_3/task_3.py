"""
Напишите функцию modify_list(l), которая принимает на вход список целых чисел, удаляет из него все нечётные значения,
а чётные нацело делит на два.
Функция должна вернуть измененный список.

Запустите свою программу и проверьте, что у вас не возникает AssertionError.
(Ключевое слово assert сверяет результат вашей функции с правильным значением)
"""


def modify_list(lst):
    i = 0
    while i < len(lst):
        if lst[i] % 2 == 0:
            lst[i] = lst[i] // 2
            i += 1
        else:
            lst.pop(i)

    return lst
    pass


assert modify_list([1, 2, 3, 4, 5, 6]) == [1, 2, 3]
assert modify_list([10, 5, 8, 3]) == [5, 4]
assert modify_list([1, 2, 3]) == [1]
