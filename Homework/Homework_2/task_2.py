"""
Используя цикл for и функцию range(), напишите программу,
которая выводит все нечетные числа от 0 до 31, включая число 31.
"""

# Решение

for number in range(0, 32):
    if number % 2 != 0:
        print(number)
