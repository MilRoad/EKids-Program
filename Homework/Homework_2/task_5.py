"""
Напишите программу, которая меняет местами первый и последний элемент списка lst местами.
"""

lst = [3, 2, 6, 12, 39, 0]

first = lst[0]
last = lst[-1]
lst[0] = last
lst[-1] = first
print(lst)