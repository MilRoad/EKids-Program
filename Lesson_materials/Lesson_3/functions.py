# Самое простое определение функции:
def my_func():
    pass
# Эта функция ничего не делает!


def my_func_1():
    print("Hello!")
# Определение функции СОЗДАЕТ функцию, но не ВЫЗЫВАЕТ функцию


# Давайте вызовем функцию:
my_func_1()


"""
Создание функции с параметрами
"""


# Создание функции с параметрами name и age
def print_name_and_age(name, age):
    print(f"Твое имя - {name}, твой возраст - {age}")


# Вызов функции
print_name_and_age("Милена", 23)  # "Милена" и 23 являются АРГУМЕНТАМИ функции print_name_and_age()


# Создание функции с параметрами со значениями по умолчанию
def print_name_and_age(name="Милена", age=23):
    print(f"Твое имя - {name}, твой возраст - {age}")


# Теперь я могу вызвать функцию, не указывая значение параметров.
print_name_and_age()
# Или указывая по одному параметру
print_name_and_age(name="Алиса")
print_name_and_age(age=18)
# Или со всеми параметрами, если я хочу заменить дефолтные значения (значения по умолчанию)
print_name_and_age("Алиса", 18)  # пример позиционных аргументов
# (значение параметров name и age определяется по позиции)

print_name_and_age(name="Алиса", age=18)  # пример именованных аргументов
# (значение параметров name и age определяется по названию)
print_name_and_age(age=18, name="Алиса")
# При использовании именованных аргументов порядок НЕ ИМЕЕТ значения!
# При использовании позиционных аргументов порядок ИМЕЕТ значение"

"""
Возвращение результата функции - ключевое слово return
"""


# Ключевое слово return завершает функцию и возвращает какое-то значение.
# Без слова return все переменные, созданные внутри функции, удаляются.
def summa(a, b):
    return a + b


summa(1, 2)
summa(34, 67)


def summa_2(a, b):
    c = a + b  # Создаем переменную 'c'
    return a + b


summa_2(1, 2)
print(c)  # Мы получим ошибку, потому что такой переменной не существует!


# Мы можем возвращать несколько значение из функции
def calculate(a, b):
    summa = a + b
    difference = a - b
    return summa, difference


s, d = calculate(3, 1)
print(s, d)


# Мы можем не возвращать ничего!
def nothing():
    return
# В данном случае тип возвращаемого значения будет None (пустота)


def while_even(number):
    while number > 0:
        if number % 2 == 0:
            print(number)
            return
        else:
            print(f"{number} is not even")
            number -= 1


def stupid_function(name):
    return
    print(f"Твое имя - {name}")


def print_person(name, age):
    if age > 120 or age < 1:
        print("Invalid age")
        return
    print(f"Name: {name}  Age: {age}")


print_person("Tom", 22)
print_person("Bob", -102)
