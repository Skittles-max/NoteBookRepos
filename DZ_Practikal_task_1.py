
def calculate_average(grades):
    try:
        return sum(grades) / len(grades)
    except ValueError:
        print("Пустой список")


def overall_gpa(list_balls):
    for grades in list_balls:
        update_list_student.append(calculate_average(grades["grades"]))
    print(f"Общий средний балл всех студентов: {sum(update_list_student) / len(list_balls)}")


def average_ball(students):
    for student in students:
        ball = calculate_average(student["grades"])
        name = student["name"]
        update_list_student.append({"name": name, "average ball": ball})
        print(f"""
Студент: {student["name"]}
Средний балл: {ball}
Статус: {"Успешен" if ball >= 75 else "Отстающий"}""")
    return update_list_student


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


def delete_students(delete_name):
    #delete_name = input("Введите имя студента которого нужно удалить "
   #                     "из списка, если таких нет то оставьте поле пустым: ")
    if delete_name:
        for student in list_students:
            if student["name"] == delete_name:
                list_students.remove(student)


list_students = [
    {"name": "Maxim", "grades": [80, 56, 89, 92]},
    {"name": "Ruslan", "grades": [78, 87, 79, 97]},
    {"name": "Olga", "grades": [89, 98, 75, 82]},
    {"name": "Anna", "grades": [94, 93, 99, 91]},
    {"name": "Mahmud", "grades": [65, 85, 35, 44]}]

add_student()
update_list_student = average_ball(list_students)
print(f'Обновленный список студентов {update_list_student}')
overall_gpa(update_list_student)
print(f"Общий средний балл всех студентов: {sum(update_list_student) / len(list_balls)}")
average_ball(list_students)
delete_name = input("Введите имя студента которого нужно удалить "
                        "из списка, если таких нет то оставьте поле пустым: ")
delete_students(delete_name)
