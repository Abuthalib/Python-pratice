# d1 ={}
#
# d2 ={1:"a",2:"b",3:"c"}
#
# d3 =dict()
#
# d4 = dict([["one",1],["two",2]])
#
# d5 = {"Abu":{"age":23,"Hometown":"Thrissur"},"Jebi":{"age":22,"Hometown":"Thrissur"}}
#
# print(d1)
# print(d2)
# print(d3)
# print(d4)
# print(d5)
#
# print(d5["Abu"])
#
# d5["Thalib"]={"age":22,"Hometown":"los"}
# print(d5)
#
# person = {
#     'first_name': 'John',
#     'last_name': 'Doe',
#     'age': 25,
#     'favorite_colors': ['blue', 'green'],
#     'active': True
# }
# # print(person["first_name"])
# # print(person["last_name"])
#
# person["gender"]  = "Male"
# #
# # print(person["gender"])
# person['age']=22
# # print(person)
#
# del person["active"]
#
# #print(person)
#
# # print(person.items())
#
# for key,value in person.items():
#     print(key,":",value)

# review question ###########

# keys = ["a","b","c"]
# values =[[1,2,],[3,4,],[5,6]]
# result ={}
# for key,values in zip(keys,values):
#     if key in result:
#         result[key].append(value)
#     else:
#         result[key] = [values]
#
# print(result)

########chat Gpt questions##########
# accessing by key

# my_dict = {"a":1,"b":2,"c":3}
# print(my_dict)
# print(my_dict["a"])
#
# ## adding new key: value
# my_dict["d"] =4
# print(my_dict)
#
# #updating values
# my_dict["a"]=10
# print(my_dict)
#
# #removing key- value pairs
# del my_dict["d"]
# print(my_dict)
#
# # iterating over key values
# for key in my_dict:
#     print(key,my_dict[key])
#
# # other way
# for key,value in my_dict.items():
#     print(key,value)

## praice dict-
keys = ["a", "b", "c", "a"]
values = [["apple", "anar"], ["bat", "ball"], ["cat", "cow"], ["abu", "amal"]]

dic = {}
for key, value in zip(keys, values):
    if key in dic:
        dic[key].append(value)
    else:
        dic[key] = value

print(dic)

del_key = "b"

for key in dic.items():
    if del_key:
        del dic[del_key]
        break
    # else:
    #     print(key,dic[key])

print(dic)

#### dict to list

my_dict = {"a": 1, "b": 2, "c": 3}
my_dict1 = {"d": 4, "e": 5, "f": 6}
list1 = [*zip(*my_dict.items())]
print(list1)

# merged dic
merge = {**my_dict, **my_dict1}
print(merge)

## inter change ing key to values
rev = {v: k for k, v in my_dict.items()}
print(rev)

# check two dict hav same key
same = set(my_dict1.keys()) == set(my_dict.keys())
print(same)


# unique char in string
stri = "helo"
unique = len(set(stri)) == len(stri)
print(unique)