"""
Напишите функцию, которая считывает знаки пунктуации в символьной строке и возвращает их количество.
К знакам пунктуации относятся символы из набора ".,;:!?".
"""


def count_punctuation_symbols(string):
    punctuation_count = 0
    for symbol in string:
        if symbol in ".,;:!?":
            punctuation_count += 1
    return punctuation_count


assert count_punctuation_symbols("Привет, ребята!") == 2
assert count_punctuation_symbols("Скажите, пожалуйста, какой сегодня день?") == 3
