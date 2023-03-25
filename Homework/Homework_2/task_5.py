"""
Напишите программу, которая меняет местами первый и последний элемент списка lst местами.
"""

lst = [3, 2, 6, 12, 39, 0]

# Решение 1
first_element = lst[0]
last_element = lst[-1]
lst[0] = last_element
lst[-1] = first_element
print(lst)

# Решение 2
lst[0], lst[-1] = lst[-1], lst[0]
print(lst)
