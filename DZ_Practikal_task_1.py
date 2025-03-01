
def calculate_average(grades):
    try:
        return sum(grades) / len(grades)
    except ValueError:
        print("Пустой список")
        pass


def overall_gpa(list_balls):
    list_average_balls = []
    for grades in list_balls:
        list_average_balls.append(calculate_average(grades["grades"]))
    print(f"Общий средний балл всех студентов: {sum(list_average_balls) / len(list_balls)}")


def average_ball(students):
    list_student = []
    for student in students:
        ball = calculate_average(student["grades"])
        name = student["name"]
        list_student.append({"name": name, "average ball": ball})
        print(f"""
Студент: {student["name"]}
Средний балл: {ball}
Статус: {"Успешен" if ball >= 75 else "Отстающий"}""")


def add_student():
    name = input("Введите имя студента: ")
    grades_input = input("Введите список баллов через запятую: ")
    try:
        grades = [int(grade.strip()) for grade in grades_input.split(",")]
    except ValueError:
        print("Неверный формат ввода")
        exit()
    new_student = {"name": name, "grades": grades}
    list_students.append(new_student)


def delete_students():
    delete_name = input("Введите имя студента которого нужно удалить "
                        "из списка, если таких нет то оставьте поле пустым: ")
    if delete_name:
        for student in list_students:
            if student["name"] == delete_name:
                list_students.remove(student)
        pass


list_students = [
    {"name": "Maxim", "grades": [80, 56, 89, 92]},
    {"name": "Ruslan", "grades": [78, 87, 79, 97]},
    {"name": "Olga", "grades": [89, 98, 75, 82]},
    {"name": "Anna", "grades": [94, 93, 99, 91]},
    {"name": "Mahmud", "grades": [65, 85, 35, 44]}]

add_student()
delete_students()
overall_gpa(list_students)
average_ball(list_students)
