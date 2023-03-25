# Кортеж - это неизменяемый список

"""
Создание кортежа
"""
# Создание пустого кортежа (tuple)
t1 = ()
t2 = tuple()

# Создание кортежа с элементами
t3 = (1, 2, 3)
t4 = ("Milena", 23, 164.5, True)


"""
Действия с кортежами
"""
# Взятие элемента по индексу
t5 = (1, 6, 3, 8)
print(t5[0])
print(t5[-1])

# Вычисление длины кортежа
length = len(t5)
print(length)

# Разложение кортежа на отдельные переменные
a, b = (1, 2)
print(a)
print(b)

# Получение подкортежей (использование срезов)
fruits = ("apple", "grape", "peach", "banana")
print(fruits[1:3])

# Перебор кортежей
tom = ("Tom", 22, "Google")
for item in tom:
    print(item)


tom = ("Tom", 22, "Google")
i = 0
while i < len(tom):
    print(tom[i])
    i += 1

# Проверка наличия значения в кортеже
user = ("Tom", 22, "Google")
name = "Tom"
if name in user:
    print("Пользователя зовут Tom")
else:
    print("Пользователь имеет другое имя")
