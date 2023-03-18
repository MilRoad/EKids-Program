"""
Создание строк
"""
# Пример с двойными кавычками
message = "Hello World!"
print(message)  # Hello World!

# Пример с одинарными кавычками
name = 'Tom'
print(name)  # Tom

'''
Это комментарий
'''

text = '''Laudate omnes gentes laudate
Magnificat in secula
Et anima mea laudate
Magnificat in secula
'''
print(text)


"""
Операции со строками
"""

s1 = "Hello "
s2 = "World!"
print(s1 + s2)  # конкатенация (сложение) строк

s3 = "name"
print(s3 * 3)  # умножение строк

s4 = "abcde"
print(s4[1])   # Взятие элемента строки (символа) по индексу

s5 = "Hello world!"
print(len(s5))  # Функция len() вычисляет длину строки

# Вставка значений в строку
user_name = "Tom"
user_age = 37
user = f"name: {user_name}  age: {user_age}"
print(user)   # name: Tom  age: 37

# Верхний регистр
s = "hello"
print(s.upper())
# Нижний регистр
s = "HELLO"
print(s.lower())

# Использование метода split()
string = "apple banana orange"
split_string = string.split()


a = 20
b = 10
c = 3
d = a < b or c > b and not a < c
print(d)

# Комментарий
