class Student:
    def __init__(self, first_name, last_name, patronymic, group, grades):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__patronymic = patronymic
        self.__group = group
        self.__grades = grades

    def get_full_name(self):
        return f"{self.__first_name} {self.__last_name} {self.__patronymic}"

    def get_group(self):
        return self.__group

    def get_grades(self):
        return self.__grades

    def average_grade(self):
        return sum(self.__grades) / len(self.__grades)

class StudentDatabase:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def view_all_students(self):
        for student in self.students:
            print(student.get_full_name())

    def view_student(self, index):
        if 0 <= index < len(self.students):
            student = self.students[index]
            print(f"ФИО: {student.get_full_name()}, Средний балл: {student.average_grade()}")
        else:
            print("Студент не найден.")

    def edit_student(self, index, first_name=None, last_name=None, patronymic=None, group=None, grades=None):
        if 0 <= index < len(self.students):
            student = self.students[index]
            if first_name:
                student.__first_name = first_name
            if last_name:
                student.__last_name = last_name
            if patronymic:
                student.__patronymic = patronymic
            if group:
                student.__group = group
            if grades:
                student.__grades = grades
        else:
            print("Студент не найден.")

    def delete_student(self, index):
        if 0 <= index < len(self.students):
            del self.students[index]
        else:
            print("Студент не найден.")

    def average_grade_by_group(self, group):
        total_grades = 0
        count = 0
        for student in self.students:
            if student.get_group() == group:
                total_grades += student.average_grade()
                count += 1
        if count > 0:
            return total_grades / count
        return 0
db = StudentDatabase()

student1 = Student("Иван", "Иванов", "Иванович", "Группа 1", [4, 5, 5, 3])
student2 = Student("Петр", "Петров", "Петрович", "Группа 2", [3, 4, 5, 4])

db.add_student(student1)
db.add_student(student2)

db.view_all_students()

db.view_student(0)

db.edit_student(0, grades=[5, 5, 5, 5])

print(db.average_grade_by_group("Группа 1"))

db.delete_student(1)
