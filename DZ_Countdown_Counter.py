def countdown_counter():
    try:
        countdown = int(input("Введите целое положительное число "))

        while countdown >= 0:
            print(countdown)
            countdown -= 1
    except ValueError:
        print("Ошибка! Введите число")

if __name__ == "__main__":
    countdown_counter()
else:
    print("Ошибка вызова функции")
