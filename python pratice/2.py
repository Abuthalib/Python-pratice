keys =["a","b","c"]
values =[["apple","apricot"],["bat","ball"],["cat","cow"]]
dic = {}
for key,value in zip(keys,values):
    if key in dic:
        dic[key].append(value)
    else:
        dic[key]= value

print(dic)

k ="a"
for key in dic.items():
    if k:
        del dic[k]
        break

print(dic)

my ={"a":1,"b":2,"c":3}
my1 ={"d":3,"e":5,"f":6}
merge = {**my,**my1}
print(merge)

ch = {v:k for k,v in merge.items()}
print(ch)
print(min(ch.values()))


d={"a":1,"b":2,"c":3}
max_key = None
max_value = float('-inf')
for key,value in d.items():
    if value > max_value:
        max_value = value
        max_key =key
print("max key :",max_key)
