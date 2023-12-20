l1 = [2,4,6,8,10]
l2 = [1,3,5,7,9,11,12]
l3 = []

la = len(l1)
lb = len(l2)
i = j = 0

while i < la and j < lb:
    if l1[i] < l2[j]:
        l3.append(l1[i])
        i += 1
    else:
        l3.append(l2[j])
        j += 1


while i < la:
    l3.append(l1[i])
    i += 1


while j < lb:
    l3.append(l2[j])
    j += 1


print(l3)
