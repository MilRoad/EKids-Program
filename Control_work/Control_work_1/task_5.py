"""
Для данного числа n < 100 закончите фразу “На лугу пасется...” одним из возможных продолжений:
“n коров”, “n корова”, “n коровы”, правильно склоняя слово “корова”.

Входные данные:
Вводится натуральное число.

Выходные данные:
Программа должна вывести правильное выражение вместе с введенным числом 'n' и одним из слов: коров, корова, коровы.


Примеры:
Вход 1: 1
Выход 1: "На лугу пасется 1 корова."

Вход 2: 2
Выход 2: "На лугу пасется 2 коровы."

Вход 3: 10
Выход 3: "На лугу пасется 10 коров."
"""

cow_number = int(input("Введите число коров: "))

"""
корова - 1, 21, 31, 41...
коровы - 2, 3, 4, 22, 23, 24, 32, ...
коров - 5, 6, 7, 8, 9, 10, 11-20, 25 ...
"""

if cow_number % 10 in [0, 5, 6, 7, 8, 9] or cow_number in range(11, 15):
    print(f"На лугу пасется {cow_number} коров.")
elif cow_number % 10 == 1:
    print(f"На лугу пасется {cow_number} корова.")
else:
    print(f"На лугу пасется {cow_number} коровы.")