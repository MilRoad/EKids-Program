class Phone:

    def __init__(self):
        self.is_on = False
        self.__color = "gray"

    def turn_on(self):
        self.is_on = True

    def call(self):
        if self.is_on:
            print('Making call...')


# Унаследованный класс
class MobilePhone(Phone):

    # Добавляем новое свойство battery
    def __init__(self):
        super().__init__()
        self._battery = 100

    # Заряжаем телефон на величину переданного значения
    def charge(self, num):
        self._battery = num
        print(f'Charging battery up to ... {self._battery}%')


# phone = Phone()
# print(dir(phone))

my_mobile_phone = MobilePhone()

print(dir(my_mobile_phone))
