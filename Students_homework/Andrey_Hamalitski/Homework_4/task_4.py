"""
Напишите функцию, которая определяет количество различных символов, встречающихся в символьной строке.
На вход функция получает строку, а на выходе количество различных символов.
Подсказка: используйте множества.

Запустите свою программу и проверьте, что у вас не возникает AssertionError.
(Ключевое слово assert сверяет результат вашей функции с правильным значением)
"""


def count_different_symbols(string):
    return len(set(string))


assert count_different_symbols("aB122AB") == 5
assert count_different_symbols("aaabbc") == 3
assert count_different_symbols("aAaAaaaA") == 2
