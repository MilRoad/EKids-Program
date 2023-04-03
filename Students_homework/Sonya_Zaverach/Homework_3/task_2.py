"""
Николай знает, что кортежи являются неизменяемыми, но он с этим не готов соглашаться.
Ученик решил создать функцию del_from_tuple(),
которая будет удалять первое появление определенного элемента из кортежа по значению и возвращать кортеж без оного.

Попробуйте повторить шедевр не признающего авторитеты начинающего программиста.
К слову, Николай не всегда уверен в наличии элемента в кортеже (в этом случае кортеж вернется функцией в исходном виде).

Запустите свою программу и проверьте, что у вас не возникает AssertionError.
(Ключевое слово assert сверяет результат вашей функции с правильным значением)
"""


def del_from_tuple(tpl, element):
    if element not in tpl:
        return tpl
    else:
        i=0
        tpl1=tuple()
        while element!=tpl[i]:
            i=i+1

        if i>0:
            tpl1=tuple(tpl[:i])

        if i<len(tpl):
            tpl1=tpl1+tuple(tpl[i+1:])

        return tpl1


assert del_from_tuple((1, 2, 3), 1) == (2, 3)
assert del_from_tuple((1, 2, 3, 1, 2, 3, 4, 5, 2, 3, 4, 2, 4, 2), 3) == (1, 2, 1, 2, 3, 4, 5, 2, 3, 4, 2, 4, 2)
assert del_from_tuple((2, 4, 6, 6, 4, 2), 9) == (2, 4, 6, 6, 4, 2)
