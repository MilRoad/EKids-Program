"""
Напишите программу, которая меняет местами первый и последний элемент списка lst местами.
"""

lst = [3, 2, 6, 12, 39, 0]
a=lst.pop(0)
b=lst.pop(len(lst)-1)
lst.append(a)
lst.insert(b,0)
print(lst)