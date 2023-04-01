"""
Напишите функцию modify_list(l), которая принимает на вход список целых чисел, удаляет из него все нечётные значения,
а чётные нацело делит на два.
Функция должна вернуть измененный список.

Запустите свою программу и проверьте, что у вас не возникает AssertionError.
(Ключевое слово assert сверяет результат вашей функции с правильным значением)
"""


def modify_list(lst):
    new_lst = []
    for item in lst:
        if item % 2 == 0:
            new_lst.append(item // 2)
    return new_lst


def modify_list_2(lst):
    return [i // 2 for i in lst if i % 2 == 0]  # list comprehension


assert modify_list([1, 2, 3, 4, 5, 6]) == [1, 2, 3]
assert modify_list([10, 5, 8, 3]) == [5, 4]
assert modify_list([1, 2, 3]) == [1]
