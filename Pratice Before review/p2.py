s ="abcdeace"
dic =dict.fromkeys((s))
un=list(dic.keys())
print(un)

my_list = [1, 2, 3, 4, 23, 8, 5, 9, 43, 54, 12, 56, 23, 12, 1, 3, 5, 6, 9, 10]
d = dict.fromkeys((my_list))
uniq = list(d.keys())
print(uniq)
sort = sorted(uniq)
print(sort)
print("min : ",sort[0])
print("max :",sort[-1])

nested = [[1,2],[3,4,5],[6,7]]
new = [item for sublist in nested for item in sublist]
print(new)

st = "Good morning abu"
rev = " ".join(st.split()[::-1])
print(rev)
