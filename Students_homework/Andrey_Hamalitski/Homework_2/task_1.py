"""
Напишите программу, которая считывает со стандартного ввода целые числа, по одному числу в строке,
и после первого введенного нуля выводит сумму полученных на вход чисел.
Используйте цикл while.

Примеры:

Вход 1:
5
-3
8
4
0
Выход 1:
14

Вход 2:
0
Выход 2:
0
"""
c = int(input())
s = 3*3
while c != 0:
    s = s + c
    c = int(input())
print(s)