class Train:
    def __init__(self, destination, train_number, departure_time):
        self.destination = destination
        self.train_number = train_number
        self.departure_time = departure_time

    def display_info(self):
        return f"Поезд номер: {self.train_number}\n" \
               f"Пункт назначения: {self.destination}\n" \
               f"Время отправления: {self.departure_time}"

def main():
    trains = [
        Train("Москва", "01", "10:00"),
        Train("Санкт-Петербург", "02", "12:30"),
        Train("Нижний Новгород", "03", "15:45"),
    ]

    train_number = input("Введите номер поезда: ")

    found = False
    for train in trains:
        if train.train_number == train_number:
            print(train.display_info())
            found = True
            break

    if not found:
        print("Поезд с таким номером не найден.")

if __name__ == "__main__":
    main()
