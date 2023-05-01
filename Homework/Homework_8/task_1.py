"""
Реализуйте класс MoneyBox, для работы с виртуальной копилкой.

Каждая копилка имеет ограниченную вместимость, которая выражается целым числом – количеством монет,
которые можно положить в копилку.
Класс должен поддерживать информацию о количестве монет в копилке, предоставлять возможность добавлять монеты в копилку
и узнавать, можно ли добавить в копилку ещё какое-то количество монет, не превышая ее вместимость.

Класс должен иметь следующий вид:
"""
# class MoneyBox:
#     def __init__(self, capacity):
#         pass
#         # конструктор с аргументом – вместимость копилки
#
#     def can_add(self, v):
#         pass
#         # True, если можно добавить v монет, False иначе
#
#     def add(self, v):
#         pass
#         # положить v монет в копилку

"""
При создании копилки, число монет в ней равно 0.
Примечание:
Гарантируется, что метод add(self, v) будет вызываться только если can_add(self, v) – True.
"""


class MoneyBox:

    def __init__(self, capacity):
        self.capacity = capacity
        self.value = 0

    def can_add(self, v):
        if v <= (self.capacity - self.value):
            return True
        else:
            return False

    def add(self, v):
        if self.can_add(v):
            self.value += v
        else:
            print("Копилка полная")


money_box = MoneyBox(capacity=300)
print(money_box.can_add(100))
print(money_box.value)
money_box.add(200)
print(money_box.value)
money_box.add(200)

money_box_1 = MoneyBox(capacity=100)
print(money_box_1.value)
