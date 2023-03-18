# В Python существуют два вида циклов - for и while

"""
Цикл while
"""

# Пример бесконечного цикла:
# while True:
#     print(1)
# Очень плохой пример! Лучше так не делать!

a = 10
while a > 0:
    print(a)
    a -= 1   # то же самое, что и a = a - 1

b = 2
while a > 0 and b < 10:  # мы можем использовать логические операции при составлении логического выражения
    print(a, b)
    a -= 1
    b += 2

while a > 12:
    print(a)


"""
Цикл for
"""

string = "Hello"

for letter in string:
    print(letter)

fruits = ["apple", "banana", "pear"]
for fruit in fruits:
    print(fruit)

numbers = [3, 2, 6, 4, 7, 19, 11]

for n in numbers:
    if n % 2 == 0:
        print(f"{n} - четное число!")

for i in range(10):
    print(i)

for index in range(len(numbers)):
    if numbers[index] % 2 == 0:
        print(f"{index} - индекс четного числа!")
        print(f"{numbers[index]} - четное число!")

