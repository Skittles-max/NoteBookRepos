print("Сложение")
sum_x = float(input("x = "))
sum_y = float(input("у = "))
print("Результат сложения: %.f" % (sum_x + sum_y))

print("Вычитание")
diff_x = float(input("x = "))
diff_y = float(input("у = "))
print("Результат вычитания: %.2f" % (diff_x - diff_y))

print("Умножение")
multiply_x = float(input("x = "))
multiply_y = float(input("у = "))
print("Результат умножения: %.2f" % (multiply_x * multiply_y))

print("Деление")
try:
    div_x = float(input("x = "))
    div_y = float(input("у = "))
    print("Результат деления: %.2f" % (div_x / div_y))
except ZeroDivisionError:
    print("Деление на 0 запрещено")
