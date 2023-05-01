class Employee:

    def __init__(self, name, surname, age, employee_id):
        self.name = name
        self.surname = surname
        self._age = age
        self.__id = employee_id

    def set_id(self, new_id):
        self.__id = new_id

    def __print_id(self):
        print(self.__id)

    def get_id(self):
        self.__print_id()


tom = Employee("Tom", "Smart", 25, 123)
tom.name = "Bob"


# public
# protected
# private
