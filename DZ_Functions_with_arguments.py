
def multiply(x, y):
    return x * y


try:
    rez = multiply(int(input("Введите значение х ")), int(input("Введите значение y ")))
    print(rez)
except ValueError:
    print("Вы ввели не число")
