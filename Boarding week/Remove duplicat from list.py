def Remove_duplicate(input_list):
    unique_list = []
    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)

    return unique_list


orginal = [1, 1, 1, 2, 3, 4, 5, 6, 6, 7, 8, 8, 9, ]
unique = Remove_duplicate(orginal)
print(unique)
