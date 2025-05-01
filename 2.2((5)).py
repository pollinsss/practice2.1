class ExampleClass:
    def __init__(self, property_one=None, property_two=None):
        self.property_one = property_one if property_one is not None else "Значение по умолчанию 1"
        self.property_two = property_two if property_two is not None else "Значение по умолчанию 2"

    def __del__(self):
        print(f"Объект {self} удален.")

if __name__ == "__main__":
    obj1 = ExampleClass("Первое значение", "Второе значение")
    print("Свойство 1:", obj1.property_one)
    print("Свойство 2:", obj1.property_two)

    obj2 = ExampleClass()
    print("Свойство 1:", obj2.property_one)
    print("Свойство 2:", obj2.property_two)

    del obj1
    del obj2
