"""
Реализуйте класс KgToPounds с параметром kg, куда передается определенное количество килограмм,
а с помощью метода to_pounds() они переводятся в фунты. (1 фунт = 2.205 кг)

Чтобы закрыть доступ к переменной “kg”, используйте инкапсуляцию и реализуйте методы:
set_kg() - для задания нового значения килограммов,
get_kg()  - для вывода текущего значения кг.

"""


class KgToPounds:

    def __init__(self, kg):
        self.__kg = kg

    def to_pounds(self):
        return self.__kg * 2.205

    def set_kg(self, new_kg):
        if not isinstance(new_kg, int):
            print("Введите целое число!")
            return
        self.__kg = new_kg

    def get_kg(self):
        return self.__kg


obj = KgToPounds(100)
print(obj.to_pounds())

print(obj.get_kg())
obj.set_kg("Привет!")

print(obj.get_kg())
obj.set_kg(22)
print(obj.get_kg())
