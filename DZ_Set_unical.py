import random


def rand_list():
    list_random = []
    for i in range(100):
        a = random.randint(1, 100)
        list_random.append(a)
    print(list_random)
    print(len(list_random))
    print(set(list_random))
    print(len(set(list_random)))


rand_list()
