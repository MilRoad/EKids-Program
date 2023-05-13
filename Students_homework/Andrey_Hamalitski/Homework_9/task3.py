    class Human:

        default_name = "Иван"
        default_age = 18

        def __init__(self, name=default_name, age=default_age):
            self.name = name
            self.age = age
            self.__money = 0
            self.__house = None

        def info(self):
            print(f"Имя: {self.name}, возраст: {self.age}, бюджет: {self.__money}, дом: {self.__house}")

        def default_info(self):
            print(f"Значения по умолчанию: {self.default_name}, {self.default_age}")

        def __make_deal(self, house_cost, discount, area):
            self.__house = {"area": area, "cost": house_cost}
            self.__money -= 100 * house_cost / (100 - discount)

        def earn_money(self, value):
            self.__money += value

        def buy_house(self, house_cost, discount, area):
            if self.__money >= (100 - discount) * house_cost:
                self.__make_deal(house_cost, discount, area)
            else:
                print("Этот дом слишком дорогой для вас")