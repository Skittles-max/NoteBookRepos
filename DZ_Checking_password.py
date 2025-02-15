
password = "qwerty"
check_passw = False
count = 6

while not check_passw:
    x = str(input("Введите пароль:"))
    if x == password:
        print("Добро пожаловать")
        check_passw = True
    else:
        count -= 1
        if count == 0:
            print("У вас не осталось попыток, повторите позже")
            break
        print(f"Неверный пароль, у вас осталось {count} попыток")
