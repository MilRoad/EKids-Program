# Создаем функцию для игры
def shop_game():
    print("Мы отправляемся за покупками!")
    shop_list = ["колбаса",  "молоко", "хлеб"]

    # Пока условие истинно (в данном случае выражение True истинно всегда)
    # Как же выбраться из цикла?
    while True:
        print()
        print("Что хотите сделать?")
        print("А. Добавить продукт в список продуктов")
        print("Б. Убрать продукт из списка продуктов по названию")
        print("В. Убрать последний продукт из списка и вывести его на экран")
        print("Г. Заменить продукт в списке продуктов")
        print("Д. Вывести список продуктов на экран")
        print("Любой другой ответ - Уйти из магазина")

        print()
        answer = input("Ваш выбор - ")

        if answer == "А" or answer == "а":
            new_product = input("Введите новый продукт: ")
            if new_product not in shop_list:
                shop_list.append(new_product)
            else:
                print("Этот продукт уже есть в списке!")
        elif answer == "Б" or answer == "б":
            remove_product = input("Введите продукт, который нужно убрать: ")
            if remove_product in shop_list:
                shop_list.remove(remove_product)
            else:
                print("Этого продукта нет в списке!")
        elif answer == "В" or answer == "в":
            if len(shop_list) > 0:
                delete_product = shop_list.pop()
                print("Вы убрали продукт - " + delete_product)
            else:
                print("Список пуст!")
        elif answer == "Г" or answer == "г":
            print("Введите номер продукта из списка, который вы хотите заменить")
            product_number = int(input("Номер продукта - "))
            print("На какой продукт хотите заменить?")
            product_name = input("Название продукта - ")
            if product_number < len(shop_list):
                if len(shop_list) > 0:
                    if product_name not in shop_list:
                        old_product_name = shop_list[product_number]
                        shop_list[product_number] = product_name
                        print("Вы заменили продукт - " + old_product_name + " на - " + product_name)
                    else:
                        print("Этот продукт уже есть в списке!")
                else:
                    print("Список пуст! Ничего заменить нельзя!")
            else:
                print("Такого номера нет в списке продуктов!")
        elif answer == "Д" or answer == "д":
            print("Список продуктов:")
            for i in range(len(shop_list)):
                print(i, shop_list[i])
        else:
            print("Уходим из магазина!")
            break


# вызываем нашу функцию игры
shop_game()
