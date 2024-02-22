Input =["eat", "tea", "tan", "ate", "nat", "bat","tab"]
result=[]

def convert(inp):
    d={}
    for  i in inp:
        if i in d:
            d[i] = d.get(i,0)+1
        else:
            d[i] = 1
    return d

for i in range(len(Input)):
    if Input[i] == " ":
        continue
    r= [Input[i]]
    a = convert(Input[i])

    for j in range(i+1,len(Input)):
        if Input[j] == " ":
            continue
        b = convert(Input[j])

        if a == b:
            check =True
        else:
            check = False
        
        if check:
            r.append(Input[j])
            Input[j]=" "
    result.append(r)
    Input[i] =" "

print(result)
