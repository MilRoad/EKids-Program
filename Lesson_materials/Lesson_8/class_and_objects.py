# Создание пустого класса
# Название класса всегда с большой буквы!
class Animal:
    pass


# Создание экземпляра (объекта) класса
animal = Animal()


# Создание класса с аттрибутами и методами
class Person:

    # Аттрибут класса
    is_primate = True

    def __init__(self, name, age):
        # Аттрибуты объекта
        self.name = name
        self.age = age

    # Методы объекта
    def say_hello(self):
        print("Hello, " + self.name)

    def is_adult(self):
        if self.age > 18:
            print("You are adult")
        else:
            print("You are child")
