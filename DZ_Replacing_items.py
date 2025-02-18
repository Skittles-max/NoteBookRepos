
def replace_line():
    list_five_line = ["Первая строка", "Вторая строка", "Третья строка", "Четвертая строка", "Пятая строка"]
    print("Начальный список: ", list_five_line)
    list_five_line[0], list_five_line[-1] = list_five_line[-1], list_five_line[0]
    print("Измененный список: ", list_five_line)


replace_line()
