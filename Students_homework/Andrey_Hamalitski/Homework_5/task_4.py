"""
1) Внимательно изучите игру hangman.py (виселица).
2) Добавьте свой набор(список) слов и передайте его в качестве аргумента в функцию hangman_game().
3) Уберите первоначальные подсказки в виде гласных букв.
4) Подумайте, зачем используется ключевой слово break внутри игры?
5) Запустите игру и поиграйте в нее.
"""
import random

technical_moments = ["питон", "программа", "компьютер", "интернет", "клавиатура", "мышь", "экран"]


def hangman_game(word_list):
    print("Добро пожаловать в игру Виселица!")

    secret = random.choice(word_list)
    guesses = ""
    turns = 5

    while turns > 0:
        missed = 0

        for letter in secret:
            if letter in guesses:
                print(letter, end=' ')
            else:
                print('_', end=' ')
                missed += 1

        if missed == 0:
            print("\nТы выиграл!")
            break

        guess = input("\nНазови букву \n")
        guesses += guess
        if guess not in secret:
            turns -= 1  # В python это то же самое, что и turns = turns - 1
            print("\nТы не угадал!")
            print(f"\nОсталось попыток: {turns}")
            if turns < 5:
                print("\n  |  ")
            if turns < 4:
                print("  O  ")
            if turns < 3:
                print(" /|\ ")
            if turns < 2:
                print("  |  ")
            if turns < 1:
                print(" / \ ")
            if turns == 0:
                print("\nТы проиграл!")
                print(f"Загаданное слово: {secret}")

    print("\nИгра окончена!")


answer = "да"
while answer == "да":
    hangman_game(technical_moments)
    print("Хочешь сыграть снова? (да/нет)")
    answer = input()