"""
1) Создайте модуль my_module.py, создайте там переменную my_variable (любое значение) и функцию my_func().
Ваша функция может делать что угодно.

2) Импортируйте модуль в этот файл, используя ключевое слово import.
3) Выведите переменную my_variable из другого модуля на экран.
4) Вызовите функцию my_func() из другого модуля в этом файле.
"""

import my_module
print (my_module.my_variable)
a = int(input())
b = int(input())
print(my_module.my_func(a, b))