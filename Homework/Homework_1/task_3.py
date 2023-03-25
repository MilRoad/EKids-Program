"""
Напишите программу, которая на вход будет принимать номер месяца,
а на выходе выводить время года, соответствующее месяцу.

Примеры:

Вход 1: 1
Выход 1: 'Зима'

Вход 2: 4
Выход 2: 'Весна'

Вход 3: 13
Выход 3: 'Времени года с таким месяцем не существует'
"""

# Решение 1
number = int(input("Введите номер месяца: "))
if number == 1 or number == 2 or number == 12:
    print("Зима")
elif number == 3 or number == 4 or number == 5:
    print("Весна")
elif number == 6 or number == 7 or number == 8:
    print("Лето")
elif number == 9 or number == 10 or number == 11:
    print("Осень")
else:
    print("Времени года с таким месяцем не существует")

# Решение 2
number = int(input("Введите номер месяца: "))
if 1 <= number <= 2 or number == 12:
    print("Зима")
elif 3 <= number <= 5:
    print("Весна")
elif 6 <= number <= 8:
    print("Лето")
elif 9 <= number <= 11:
    print("Осень")
else:
    print("Времени года с таким месяцем не существует")

# Решение 3 (со списками)
number = int(input("Введите номер месяца: "))
if number in [1, 2, 12]:
    print("Зима")
elif number in [3, 4, 5]:
    print("Весна")
elif number in [6, 7, 8]:
    print("Лето")
elif number in [9, 10, 11]:
    print("Осень")
else:
    print("Времени года с таким месяцем не существует")
