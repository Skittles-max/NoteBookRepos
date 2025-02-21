
def calculate_average(grades):
    return sum(grades) / len(grades)


def overall_gpa():
    list_average_balls = []
    for grades in list_students:
        list_average_balls.append(calculate_average(grades["grades"]))

    print(f"Общий средний балл всех студентов: {sum(list_average_balls) / len(list_students)}")


def average_ball():
    for student in list_students:
        ball = calculate_average(student["grades"])
        name = student["name"]
        list_average_ball.append({"name": name, "average ball": ball})
        print(f"""
Студент: {student["name"]}
Средний балл: {ball}
Статус: {"Успешен" if ball >= 75 else "Отстающий"}""")
    return list_average_ball


def add_delete_student():
    name = input("Введите имя студента: ")
    grades_input = input("Введите список баллов через запятую: ")
    grades = [ int(grade.strip()) for grade in grades_input.split(",")]
    new_student = {"name": name, "grades": grades}
    list_students.append(new_student)
    delete_name = input("Введите имя студента которого нужно удалить "
                        "из списка, если таких нет то оставьте поле пустым: ")
    if delete_name:
        for student in list_students:
            if student["name"] == delete_name:
                list_students.remove(student)
    else:
        pass

    print(list_students)


list_students = [
    {"name": "Maxim", "grades": [80, 56, 89, 92]},
    {"name": "Ruslan", "grades": [78, 87, 79, 97]},
    {"name": "Olga", "grades": [89, 98, 75, 82]},
    {"name": "Anna", "grades": [94, 93, 99, 91]},
    {"name": "Mahmud", "grades": [65, 85, 35, 44]}]

list_average_ball = []
average_ball()
add_delete_student()
overall_gpa()

