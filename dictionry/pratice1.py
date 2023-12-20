keys = ["a", "b", "c"]
values = [["apple", "anar"], ["bat", "ball"], ["cat", "cow"]]
dic = {}
for key, value in zip(keys, values):
    if key in dic:
        dic[key].append(value)
    else:
        dic[key] = value

print(dic)

del_key = "c"
for key in dic.items():
    if del_key:
        del dic[del_key]
        break

print(dic)

########dict -->list###########
my_dict = {"a": 1, "b": 2, "c": 3}
my_dict1 = {"d": 4, "e": 5, "f": 6}
list1 = [*zip(*my_dict.items())]
print(list1)

##########merge ########
merge = {**my_dict, **my_dict1}
print(merge)

######## interchnage key and value########
rev = {v: k for k, v in my_dict.items()}
print(rev)

######### check if there is same key######
same = set(my_dict1.keys()) == set(my_dict.keys())
print(same)

#########uniq string
string ="hai"
unique = len(set(string)) == len(string)
print(unique)