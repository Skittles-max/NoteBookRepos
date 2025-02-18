def addition_list(list_1, list_2):
    if len(list_1) > len(list_2):
        sum_lists = list_1
        for i in range(len(list_2)):
            sum_lists[i] += list_2[i]

    else:
        sum_lists = list_2
        for i in range(len(list_1)):
            sum_lists[i] += list_1[i]
    print(sum_lists)


addition_list([1, 2, 3], [1, 4, 5, 6])
