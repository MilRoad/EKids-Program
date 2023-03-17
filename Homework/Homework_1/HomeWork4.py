b = int(input("Минимальное время сна: "))
c = int(input("Максимальное время сна: "))
a = int(input("Время сна Ани: "))


if a > c:
    print("Пересып")
elif a < b:
    print("Недосып")
elif b <= a <= c:
    print("Хороший сон")