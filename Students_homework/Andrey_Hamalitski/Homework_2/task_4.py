"""
Напишите программу, на вход которой подается одна строка с целыми числами. Программа должна вывести сумму этих чисел.

Используйте метод split() строки и цикл for или while.

Пример:

Вход:
4 0 9 3
Выход:
16
"""
e = [ int(y) for y in input().split()]
g = 0
t = len(e)-1
for y in range(0,t+1):
    g = g + e[y]
print(g)