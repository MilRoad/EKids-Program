"""
Найдите количество положительных элементов в данном списке.

Входные данные:
Вводится список чисел. Все числа списка находятся на одной строке.

Выходные данные:
Выведите ответ на задачу.

Пример:
Вход: 1 -2 3 -4 5
Выход: 3
"""

lst = input("Введите последовательность чисел: ").split()
positive_count = 0
for item in lst:
    if int(item) > 0:
        positive_count += 1
print(f"Количество положительных элементов: {positive_count}")
