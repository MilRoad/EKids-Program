"""
Напишите программу, на вход которой подается одна строка с целыми числами. Программа должна вывести сумму этих чисел.

Используйте метод split() строки и цикл for или while.

Пример:

Вход:
4 0 9 3
Выход:
16
"""

# Решение
list_of_numbers = input().split()
summa = 0
for item in list_of_numbers:
    summa += int(item)
print(summa)
