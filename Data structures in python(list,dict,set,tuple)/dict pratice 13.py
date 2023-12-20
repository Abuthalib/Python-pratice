keys = ["a","b","c","a"]
values = [["apple","apricot"],["bat","ball"],["cat","cow"]]

dic = {}
for key,value in zip(keys,values):
    if key in dic:
        dic[key].append(value)
    else:
        dic[key]=value

print(dic)

del_key  = "a"
for key in dic.items():
    if del_key:
        del dic[del_key]
        break

print(dic)

my ={"a":1,"b":2,"c":3}
my1 ={"d":3,"e":5,"f":6}

merge = {**my,**my1}
print(merge)

i_chnage ={v:k for k,v in my.items()}
print(i_chnage)

s = "hello"
uniqe = len(set(s)) == len(s)
print(uniqe)



abc={"d":3,"e":5,"f":6}
a=abc.values()
print(a)