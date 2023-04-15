"""
1) Создайте модуль my_module.py, создайте там переменную my_variable (любое значение) и функцию my_func().
Ваша функция может делать что угодно.

Если вы уже создавали модуль my_module.py в прошлом задании, пропустите первый шаг.

2) Импортируйте переменную my_variable и функцию my_func(), используя ключевое слово from.
3) Выведите переменную my_variable из другого модуля на экран.
4) Вызовите функцию my_func() из другого модуля в этом файле.
"""
from my_module import my_variable
from my_module import my_func
print(my_variable)
my_func()