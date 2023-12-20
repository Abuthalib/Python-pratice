my_list = [1,11,34,55,33,56,77,86,5,5,42,65,75,1,4,3,6]
dic = dict.fromkeys(my_list)
unique = list(dic.keys())
print(unique)

sortedlist = sorted(unique)
print(sortedlist)
print(sortedlist[0])
print(sortedlist[-1])

s= "malayalam"
is_palindrome = s ==s[::-1]
if is_palindrome:
    print("its palindrome")
else:
    print("its not palindrome")

nested =[[1,2],[3,4,5],[6,7]]
new = [item for sublist in nested for item in sublist]
print(new)


st = "good morning abu"
rev = " ".join(st.split()[::-1])
print(rev)