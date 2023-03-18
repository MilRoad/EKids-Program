# Списки - это изменяемый тип данных в языке Python.

"""
Создание списков
"""
# Для создания списков используются квадратные скобки []:
l1 = []  # пустой список
l2 = list()  # тоже пустой список

l3 = ["Tom", "Andy", "Max"]  # список из строк
l4 = [1, "Tom", True]  # список из разных типов данных

"""
Операции со списками
"""

# Part 1
fruits = ["apple", "orange", "banana", "grape"]

first_fruit = fruits[0]  # взятие элемента списка по индексу
# Обратите внимание! Счет в Python начинается с НУЛЯ!
# fruits[0] - это первый элемент списка!
last_fruit = fruits[3]
last_fruit_2 = fruits[-1]

print(fruits[1:3])  # использование срезов для взятия части списка

fruits_length = len(fruits)  # возвращает длину списка (количество элементов в списке)

fruits.append("pineapple")  # добавление нового элемента в конец списка
print(fruits)

fruits.insert(2, "pear")  # добавление нового элемента в список на указанную позицию

fruits.pop(0)  # удаление элемента списка по индексу
# метод pop() не только удаляет элемент, но и возвращает его!


# Part 2
numbers = [9, 4, 67, 23, 0, 1]

print(max(numbers))  # возвращает максимальный элемент списка
print(min(numbers))  # возвращает минимальный элемент списка

numbers.sort()  # метод sort() сортирует список в порядке возрастания
print(numbers)

# или можно использовать функцию sorted()
print(sorted(numbers, reverse=True))


# Part 3
# Проверка наличия элемента в списке
students = ["Tom", "Andy", "Max"]

if "Tom" in students:
    print("Tom is a student")

if "Elsa" not in students:
    print("Elsa is not a student")
