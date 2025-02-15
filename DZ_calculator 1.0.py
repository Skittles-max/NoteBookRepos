try:
    sign_x = input("Знак (+,-,*,/): ")
    if sign_x in ("+", "-", "*", "/"):
        num_x = float(input("x = "))
        num_y = float(input("y = "))
        if sign_x == "+":
            print("%.2f" % (num_x + num_y))
        elif sign_x == "-":
            print("%.2f" % (num_x - num_y))
        elif sign_x == "*":
            print("%.2f" % (num_x * num_y))
        elif sign_x == "/":
            print("%.2f" % (num_x / num_y))
    else:
        print("Неверный знак")
except ZeroDivisionError:
    print("Делить на 0 нельзя")
except ValueError:
    print("Ошибка, введите целое или дробное число")
