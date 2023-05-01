class Person:

    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def say_hello(self):
        print("Привет, " + self.name)

    def is_adult(self):
        if self.age > 18:
            print("Ты совершеннолетний")
        else:
            print("Ты еще ребенок")


class Student(Person):

    def what_grade(self):
        if self.age == 7:
            print("Ты в первом классе")
        elif self.age == 8:
            print("Ты во втором классе")
        elif self.age == 9:
            print("Ты в третьем классе")
        elif self.age == 10:
            print("Ты в четвертом классе")
        else:
            print("Ты в старшей школе")


student = Student("Милена", "Лаисцева", 24)
student.what_grade()
student.is_adult()


class MathStudent(Student):
    pass
