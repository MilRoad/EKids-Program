m = int(input("Введите время в минутах: "))


a = str(m // 60)
print(a + " часа")
b = str(m % 60.0)
print(b + " минут")