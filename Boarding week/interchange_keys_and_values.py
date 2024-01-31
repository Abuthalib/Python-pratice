def inter_change(input_dic):
    fliped = {}
    for key, value in input_dic.items():
        fliped[value] = key
    return fliped


orginal = {"A": 1, "B": 2}
flip = inter_change(orginal)
print(flip)
