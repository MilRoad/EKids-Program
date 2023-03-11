# Функция input() всегда создает строку
# Но мы можем поменять тип переменной!
# Чтобы строка стала числом, используй функцию int()!
month = int(input("Введите номер месяца: "))


if month == 1:
    print("Это январь!")
elif month == 2:
    print("Это февраль!")
elif month == 3:
    print("Это март!")
elif month == 4:
    print("Это апрель!")
elif month == 5:
    print("Это май!")
elif month == 6:
    print("Это июнь!")
elif month == 7:
    print("Это июль!")
elif month == 8:
    print("Это август!")
elif month == 9:
    print("Это сентябрь!")
elif month == 10:
    print("Это октябрь!")
elif month == 11:
    print("Это ноябрь!")
elif month == 12:
    print("Это декабрь!")
else:
    print("Такого месяца не существует!")