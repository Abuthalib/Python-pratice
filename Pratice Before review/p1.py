keys = ["a", "b", "c"]
values = [["apple", "apricot"], ["bat", "ball"], ["cat", "cow"]]

di = {}

for key, value in zip(keys, values):
    if key in di:
        di[key].append(value)
    else:
        di[key] = value

print(di)

del_key = "a"
for key in di.items():
    if del_key:
        del di[del_key]
        break

print(di)

my ={"a":1,"b":2,"c":3}
my1 ={"d":3,"e":5,"f":6}

merge ={**my,**my1}
print(merge)

i_change ={v:k for k,v in my.items()}
print(i_change)
