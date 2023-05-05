"""
Одно из применений множественного наследование – расширение функциональности класса каким-то заранее определенным способом.
Например, если нам понадобится логировать какую-то информацию при обращении к методам класса.
Логирование - запись логов (действий)Б которые позволяют восстановить цепочку событий.

Рассмотрим класс Loggable:
"""
import time


class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))

"""
У него есть ровно один метод log, который позволяет выводить в лог (в данном случае в консоль) какое-то сообщение, 
добавляя при этом текущее время.
Реализуйте класс LoggableList, отнаследовав его от классов list и Loggable таким образом, 
чтобы при добавлении элемента в список посредством метода append в лог отправлялось сообщение, 
состоящее из только что добавленного элемента.
"""
class LoggableList(list, Loggable):
    def append(self, element):
        super().append(element)
        self.log(element)