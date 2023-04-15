"""
Напишите функцию sum_range(start, end),
которая суммирует все целые числа от значения «start» до величины «end» включительно, и возвращает эту сумму.
Если пользователь задаст первое число большее чем второе, просто поменяйте их местами.

Запустите свою программу и проверьте, что у вас не возникает AssertionError.
(Ключевое слово assert сверяет результат вашей функции с правильным значением)
"""


def sum_range(start, end):
    s = 0
    if start > end :
        start, end = end, start
    while start <= end:
        s = s + start
        start = start + 1
    return s


assert sum_range(2, 12) == 77
assert sum_range(-4, 4) == 0
assert sum_range(2, 3) == 5


print (sum_range(int(input()), int(input())))

