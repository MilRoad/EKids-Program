"""
1) Импортируйте встроенный модуль math, используя ключевое слово import.
2) Импортируйте функцию randint() из встроенного модуля random, используя ключевое слово from.

Функция randint(a, b) получается на вход два числа - a и b, и рандомно выбирает число между a и b. (a < b)
Возведите в рандомную степень рандомное число, полученные с помощью функции randint().
Для возведения в степень воспользуйтесь функций pow() из встроенного модуля math.
"""
import math
from random import randint

a = randint(1, 10)
b = randint(2, 5)

print(math.pow(a, b))
