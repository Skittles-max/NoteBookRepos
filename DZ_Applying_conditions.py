def sum_even():
    rezult = []
    for i in range(1, 101):
        if i % 2 == 0:
            rezult.append(i)
    print(sum(rezult))


def sq_odd_num():
    list_square = []
    for i in range(1, 11):
        if i % 2 != 0:
            list_square.append(i**2)
    print(list_square)


def negative_value():
    list_num = []
    while True:
        num = int(input("Введите число: "))
        if num < 0:
            break
        else:
            list_num.append(num)
    print(f"Вы угадали число с {len(list_num)} раз")


if __name__ == "__main__":
    sum_even()
    sq_odd_num()
    negative_value()
