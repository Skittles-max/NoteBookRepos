
try:
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))
    rezult = num1 / num2;
except ValueError:
    print("Ошибка, введите число")
except ZeroDivisionError:
    print("На ноль делить нельзя");
finally:
    print(rezult)
    print("Вы все посчитали? Закройте окно.")