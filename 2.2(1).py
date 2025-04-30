class Student:
    def __init__(self, last_name, birth_date, group_number, grades):
        self.last_name = last_name
        self.birth_date = birth_date
        self.group_number = group_number
        self.grades = grades
    def change_last_name(self, new_last_name):
        self.last_name = new_last_name
    def change_birth_date(self, new_birth_date):
        self.birth_date = new_birth_date
    def change_group_number(self, new_group_number):
        self.group_number = new_group_number
    def display_info(self):
        print(f"Фамилия: {self.last_name}")
        print(f"Дата рождения: {self.birth_date}")
        print(f"Номер группы: {self.group_number}")
        print(f"Успеваемость: {self.grades}")
def main():
    student = Student("Иванов", "2000-01-01", "101", [4, 5, 3, 4, 5])

    print("Информация о студенте:")
    student.display_info()

    student.change_last_name("Петров")
    student.change_birth_date("2000-02-02")
    student.change_group_number("102")

    print("\nОбновленная информация о студенте:")
    student.display_info()

    search_last_name = input("\nВведите фамилию студента для поиска: ")
    search_birth_date = input("Введите дату рождения студента для поиска (YYYY-MM-DD): ")

    if student.last_name == search_last_name and student.birth_date == search_birth_date:
        print("Студент найден:")
        student.display_info()
    else:
        print("Студент не найден.")


if __name__ == "__main__":
    main()
