class IntegerStorage:
    def __init__(self, num1=0, num2=0):
        self.num1 = num1
        self.num2 = num2

    def display(self):
        print(f"Число 1: {self.num1}, Число 2: {self.num2}")

    def update(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def sum(self):
        return self.num1 + self.num2

    def max_value(self):
        return max(self.num1, self.num2)

if __name__ == "__main__":
    storage = IntegerStorage(5, 10)
    storage.display()

    storage.update(15, 20)
    print("После обновления значений:")
    storage.display()

    total = storage.sum()
    print(f"Сумма значений: {total}")

    maximum = storage.max_value()
    print(f"Наибольшее значение: {maximum}")
