"""
Используя цикл for и функцию range(), напишите программу,
которая выводит все нечетные числа от 0 до 31, включая число 31.
"""
for n in range(32):
        if n % 2 != 0:
            print(f"{n}")