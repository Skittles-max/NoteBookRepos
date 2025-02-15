def max_number(a, b):
    if a >= b:
        return a
    else:
        return b


def empty_function():
    pass


def even_numbers(n):
    list_generation = []
    for number in range(n + 1):
        if number % 2 == 0:
            list_generation.append(number)
            yield number


def max_number_test():
    assert max_number(5, 4) == 5, "Ошибка, max_number(5, 4) должна быть равна 5"
    assert max_number(2, 7) == 7, "Ошибка, max_number(2, 7) должна быть равна 7"
    assert max_number(-1, 2) == 2, "Ошибка, max_number(-1, 2) должна быть равна 2"
    assert max_number(-2, -5) == -2, "Ошибка, max_number(-2, -5) должна быть равна -2"


if __name__ == "__main__":
    max_number_test()
    test_even = even_numbers(8)
    for even in test_even:
        print(even)
