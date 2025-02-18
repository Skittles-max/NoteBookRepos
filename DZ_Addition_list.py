
def addition_list(list_1, list_2):
    new_list = []
    for i in list_1:
        for j in list_2:
            new_list.append(i + j)
    print(new_list)


addition_list([1, 2, 3, 4, 5, 6, 7], [7, 6, 5, 4, 3, 2, 1])
