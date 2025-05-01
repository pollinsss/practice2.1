class Counter:
    def __init__(self, initial_value=0):
        self._value = initial_value

    def increase(self):
        self._value += 1

    def decrease(self):
        self._value -= 1

    @property
    def value(self):
        return self._value
if __name__ == "__main__":
    counter_default = Counter()
    print("Счетчик со значением по умолчанию:", counter_default.value)

    counter_default.increase()
    print("После увеличения:", counter_default.value)

    counter_default.decrease()
    print("После уменьшения:", counter_default.value)

    counter_custom = Counter(15)
    print("Счетчик с произвольным значением:", counter_custom.value)

    counter_custom.increase()
    print("После увеличения:", counter_custom.value)

    counter_custom.decrease()
    print("После двух уменьшений:", counter_custom.value)
