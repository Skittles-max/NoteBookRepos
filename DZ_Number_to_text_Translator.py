def number_to_text():

    try:
        number = int(input("Введите число от 1 до 5"))

        if number == 1:
            print("One")
        elif number == 2:
            print("Two")
        elif number == 3:
            print("Three")
        elif number == 4:
            print("Four")
        elif number ==  5:
            print("Five")
        else:
            print("Вы ввели число не входящее в диапазон")
    except ValueError:
        print("Вы ввели не число")


if __name__ == "__main__":
    number_to_text()
