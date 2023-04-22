# Создаем функцию для игры
# Почему функцию? Чтобы повторять игру несколько раз!
def millionaire_game():
    # Пустой вызов функции print() просто выводит пустую строку.
    # Используется для красоты
    print()
    print("Привет! Это игра Кто хочет стать миллионером!")
    print("Как тебя зовут?")
    name = input("Ответ - ")

    print()
    print("Приятно познакомиться, " + name)
    # Создаем переменную bank, куда будем записывать выигрыш
    bank = 0

    print("И так, внимание, первый вопрос на 1000 рублей!")
    print()
    print("С какого месяца начинается зима?")
    print("А. январь")
    print("Б. октябрь")
    print("В. декабрь")
    print("Г. февраль")

    print()
    # Считываем ответ
    answer = input("Ответ - ")
    # Правильный ответ - вариант В
    # Если ввели заглавную "В" ИЛИ маленькую "в",
    # Считаем этот ответ правильным
    if answer == "В" or answer == "в":
        print("Это правильный ответ!")
        # Увеличиваем выигрыш на 1000 рублей
        bank += 1000  # bank = bank + 1000
        print("Ваш выигрыш: " + str(bank))
    else:
        # Если ответ неправильный, игра заканчивается
        print("К сожалению, это неправильный ответ!")
        print("Игра окончена!")
        print("Ваш выигрыш: " + str(bank))
        # Ключевое слово return используется для возвращения каких-то значений
        # В данном случае return ничего не возвращает, а просто заканчивает действие нашей функции
        return

    print()
    print("И так, внимание, второй вопрос на 5000 рублей!")
    print()
    print("Когда наступает Новый год?")
    print("А. 31 декабря")
    print("Б. 1 января")
    print("В. 2 января")
    print("Г. 30 декабря")

    print()
    answer = input("Ответ - ")
    if answer == "Б" or answer == "б":
        print("Это правильный ответ!")
        bank += 5000
        print("Ваш выигрыш: " + str(bank))
    else:
        print("К сожалению, это неправильный ответ!")
        print("Игра окончена!")
        print("Ваш выигрыш: " + str(bank))
        return

    print()
    print("И так, внимание, третий вопрос на 10000 рублей!")
    print()
    print("Что является главным символом Нового года?")
    print("А. мандарины")
    print("Б. снег")
    print("В. подарки")
    print("Г. ёлка")

    print()
    answer = input("Ответ - ")
    if answer == "Г" or answer == "г":
        print("Это правильный ответ!")
        bank += 10000
        print("Ваш выигрыш: " + str(bank))
    else:
        print("К сожалению, это неправильный ответ!")
        print("Игра окончена!")
        print("Ваш выигрыш: " + str(bank))
        return

    print()
    print("Это был последний вопрос. Игра окончена!")
    print("Наш победитель - " + name)
    return


user_answer = "да"
# Пока ответ равен "да", будем играть в игру
while user_answer == "да":
    millionaire_game()
    print("Хочешь сыграть снова? (да/нет)")
    user_answer = input()