key = ["A","B","C"]
values =[["Apple"],["Bat"],["Cat"]]

dicts={}

for key,value in zip(key,values):
    if key in dicts:
        dicts[key].append(value)
    else:
        dicts[key] = [value]
print(dicts)