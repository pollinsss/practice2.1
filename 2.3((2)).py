class Worker:
    def __init__(self, name, age, position):
        self.__name = name
        self.__age = age
        self.__position = position

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_position(self):
        return self.__position
worker = Worker("Иван", 27, "Инженер")
print(worker.get_name())
print(worker.get_age())
print(worker.get_position())
