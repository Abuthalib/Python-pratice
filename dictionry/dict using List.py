key =["A","B","C","B"]
value =[["Apple","Anaar"],["Bat","Ball"],["Cat","Cow"],"Bus"]

dic ={}
for key, value in zip(key,value):
    if key in dic:
        dic[key].append(value)
    else:
        dic[key] = value

print(dic)

del_key = "B"
for key in dic.items():
    if del_key:
        del dic[del_key]
        break
print(dic)