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

    def set_kg(self, kg):
        self.__kg = kg

    def get_kg(self):
        return self.__kg

    def to_pounds(self):
        return self.__kg * 2.205