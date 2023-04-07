"""
Напишите функцию sum_range(start, end),
которая суммирует все целые числа от значения «start» до величины «end» включительно, и возвращает эту сумму.
Если пользователь задаст первое число большее чем второе, просто поменяйте их местами.

Запустите свою программу и проверьте, что у вас не возникает AssertionError.
(Ключевое слово assert сверяет результат вашей функции с правильным значением)
"""


def sum_range(start, end):
    if start > end:
        start, end = end, start
    summa = 0
    for i in range(start, end + 1):
        summa += i
    return summa


assert sum_range(2, 12) == 77
assert sum_range(-4, 4) == 0
assert sum_range(3, 2) == 5
