# Встроенный модуль random позволяет делать случайный выбор
import random

# Создаем наш список слов для игры
# Фрукты
fruits = ["апельсин", "яблоко", "груша", "банан", "виноград", "манго", "мандарин"]
# Овощи
vegetables = ["огурец", "помидор", "кабачок", "баклажан", "морковь", "картофель"]


class HangmanGame:

    def __init__(self, word_list, guesses):
        self.word_list = word_list
        self.guesses = guesses

    def hangman(self):
        print("Добро пожаловать в игру Виселица!")

        # С помощью модуля random рандомно выбираем слово из списка
        secret = random.choice(self.word_list)
        turns = 5

        # Пока количество попыток больше 0
        while turns > 0:
            # Переменная missed отвечает за количество не угаданных (пропущенных) букв
            missed = 0
            # Проходим по буквам в загаданном слове secret
            for letter in secret:
                # Если буква из секрета содержится в подсказках или введенных буквах
                if letter in self.guesses:
                    # Выводим эту букву на экран
                    print(letter, end=' ')
                else:
                    # Если буквы из секрета нет во введенных буквах,
                    # выводим нижнее подчеркивание (пропуск) на экран
                    print('_', end=' ')
                    missed += 1

            # Если не угаданных (пропущенных) букв не осталось, вы выиграли
            if missed == 0:
                print("\nТы выиграл!")
                break

            # Догадка - ваша введенная буква
            guess = input("\nНазови букву \n")
            # Добавляем букву к подсказкам/угадываниям
            self.guesses += guess

            # Если введенная буква не содержится в секретном слове
            if guess not in secret:
                # Уменьшаем количество попыток на 1
                turns -= 1  # В python это то же самое, что и turns = turns - 1
                print("\nТы не угадал!")
                print(f"\nОсталось попыток: {turns}")
                # Сравниваем количество оставшихся попыток, чтобы вывести человечка на экран
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
                # Если количество попыток закончилось (ошиблись 5 раз),
                # Игрок проиграл
                if turns == 0:
                    print("\nТы проиграл!")
                    print(f"Загаданное слово: {secret}")

    def start_game(self):
        answer = "да"
        while answer == "да":
            self.hangman()
            print("Хочешь сыграть снова? (да/нет)")
            answer = input()


game_1 = HangmanGame(word_list=fruits, guesses="ауоыиэяюеё")
game_1.start_game()

game_2 = HangmanGame(word_list=vegetables, guesses="")
