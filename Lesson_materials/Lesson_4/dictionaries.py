"""
Создание словаря
"""
# Создание пустого словаря
d1 = {}
d2 = dict()

info = {
    "name": "Milena",
    "age": 23
}

info_2 = {
    1: 2,
    "1": 2,
}

"""
Операции со словарями
"""

# Взятие элемента словаря по ключу
person_info = {
    "name": "Milena",
    "age": 23,
    "hobbies": ["video games", "drawing", "reading"]
}

print(person_info["name"])
# или
print(person_info.get("name"))

# В чем разница между взятием элемента по ключу напрямую и использованием метода get?


# Добавление нового элемента в словарь
person_info["last_name"] = "Laistseva"

# Изменение существующего элемента словаря
person_info["age"] = 24
print(person_info)

# Удаление элемента по ключу
del person_info["last_name"]
person_info.pop("name")
"""
pop(key): удаляет элемент по ключу key и возвращает удаленный элемент. 
Если элемент с данным ключом отсутствует, то генерируется исключение KeyError

pop(key, default): удаляет элемент по ключу key и возвращает удаленный элемент. 
Если элемент с данным ключом отсутствует, то возвращается значение default.
"""

# Если необходимо удалить все элементы, можно воспользоваться методом clear()
person_info.clear()

# Расширение словаря
d3 = {"name": "Milena", "age": 23}
d4 = {"last_name": "Laistseva"}
d3.update(d4)


"""
Перебор словаря
"""
person_info = {
    "name": "Milena",
    "age": 23,
    "hobbies": ["video games", "drawing", "reading"]
}

for key, value in person_info.items():
    print(f"{key}: {value}")

for key in person_info.keys():
    print(key)

for value in person_info.values():
    print(value)
