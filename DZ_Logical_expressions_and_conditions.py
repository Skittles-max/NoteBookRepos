def vote():
    age = int(input("Введите ваш возраст").strip())
    citizenship = input("Являетесь ли вы гражданином РФ?").upper().strip()
    disqualification = input("У вас есть какие либо ограничения для голосования?(Да/Нет)").upper()

    if age >= 18 and citizenship == "ДА" and disqualification == "НЕТ":
        print("Успешного голосования")
    else:
        print("Вы не можете голосовать")

if __name__ == '__main__':
    vote()
else:
    print("Ошибка вызова функции голосования")
