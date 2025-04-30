class Student:
    def __init__(self, surname, birth_date, group_number, grades):
        self.surname = surname
        self.birth_date = birth_date
        self.group_number = group_number
        self.grades = grades
    def change_surname(self, new_surname):
        self.surname = new_surname
    def change_birth_date(self, new_birth_date):
        self.birth_date = new_birth_date
    def change_group_number(self, new_group_number):
        self.group_number = new_group_number
    def display_info(self):
        return f"Фамилия: {self.surname}, Дата рождения: {self.birth_date}, Номер группы: {self.group_number}, Успеваемость: {self.grades}"

def main():
    student1 = Student("Иванов", "01.01.2000", "Группа 1", [4, 5, 3, 4, 5])
    student2 = Student("Петров", "02.02.2001", "Группа 2", [5, 5, 5, 5, 5])

    student1.change_surname("Сидоров")
    student1.change_birth_date("10.10.2000")
    student1.change_group_number("Группа 3")

    print(student1.display_info())
    print(student2.display_info())

    search_surname = input("Введите фамилию студента: ")
    search_birth_date = input("Введите дату рождения студента: ")

    if (search_surname == student1.surname and
        search_birth_date == student1.birth_date):
        print(student1.display_info())
    elif (search_surname == student2.surname and
          search_birth_date == student2.birth_date):
        print(student2.display_info())
    else:
        print("Студент не найден.")

if __name__ == "__main__":
    main()
