# eg:1  creatig dictinory
# dict1 = {101: "x",102:"y",103:"z"}
# print(dict1)

# eg2: access items from dictionary
# dict1 = {
#     "brand": "hundai",
#     "model": "i10",
#     "year": 2021
# }
# print(dict1["brand"])
# print(dict1["model"])
#
# #using get ()
# x=dict1.get("year")
# print(x)

# eg:3  change values in dictionary
# dict1 = {"brand": "hundai", "model": "i10", "year": 2021}
# print(dict1)
# dict1["year"]=2023
# print(dict1)

# eg :4 reading items from dictinoary using loop
# dict1 = {
#     "brand": "hundai",
#     "model": "i10",
#     "year": 2021
# }
# for i in dict1: # print only key
#     print(i)
#
# for i in dict1: # print only values
#     print(dict1[i])

# for i in dict1.values(): # print only key
#     print(i)

# for i in dict1: # print in actual format
#     print(i,":",dict1[i])
#
# for x,y in dict1.items():
#     print(x,":",y)


# eg :5  check key is exesting or not
# dict1 = {
#     "brand": "hundai",
#     "model": "i10",
#     "year": 2021
# }
# if "model" in dict1:
#     print("yes")
# else:
#     print("No")


# eg :6 count of items
# dict1 = {
#     "brand": "hundai",
#     "model": "i10",
#     "year": 2021
# }
#print(len(dict1))


# eg: 7 adding items to dict
# dict1 = {
#     "brand": "hundai",
#     "model": "i10",
#     "year": 2021
# }
# print(dict1)
# dict1["color"] ="red"
# print(dict1)


# eg:8  remove item from dictinoary
# dict1 = {
#     "brand": "hundai",
#     "model": "i10",
#     "year": 2021
# }
# print(dict1)
# dict1.pop("year")
# print(dict1)

# del dict1["model"]
# print(dict1)

# del dict1
# print(dict1)

# dict1.clear()
# print(dict1)

# eg:9 copy dictinory
dict1 = {
    "brand": "hundai",
    "model": "i10",
    "year": 2021
}
# using copy()
dict2=dict1.copy()
print(dict2)
#with out using copy function
# dict2 = dict1
# print(dict2)



# eg :10
