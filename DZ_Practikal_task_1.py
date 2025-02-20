

list_students = [
    {"name": "Maxim", "grades": [80, 56, 89, 92]},
    {"name": "Ruslan", "grades": [78, 87, 79, 97]},
    {"name": "Olga", "grades": [89, 98, 75, 82]},
    {"name": "Anna", "grades": [94, 93, 99, 91]},
    {"name": "Mahmud", "grades": [65, 85, 35, 44]}]


def calculate_average(grades):
    return sum(grades) / len(grades)


for student in list_students:
    average_ball = calculate_average(student["grades"])
    print(f"""Студент: {student["name"]} 
Средний балл: {average_ball}
Статус: {"Успешен" if average_ball >= 75 else "Отстающий"}""")


def overall_gpa():
    len_student = 0
    list_average_ball = []
    for grades in list_students:
        len_student += 1
        list_average_ball.append(calculate_average(grades["grades"]))

    print(f"Общий средний балл всех студентов: {sum(list_average_ball) / len_student}")

overall_gpa()
