# l1=[]
# l2=[1,2,"3",4]
# l3 = list()
# l4 = list((1,2,3))
# numbers=[1,2,3,4,5,67,8,9]
# print(l1)
# print(l2)
# print(l3)
# print(l4)
#
# #accessing list
# print(l2[0])
#
# print(l2[0:])
#
#
# #append and remove
# l2.append(5)
# print(l2)
# l2.remove('3')
# print(l2)
#
# #list py tutorials
# print(numbers[::-1])
# numbers[1] //= 2
# print(numbers)
#
# numbers.append(100)
# print(numbers)
#
# numbers.insert(2,200)
# print(numbers)
#
# del numbers[0]
# print(numbers)
#
# numbers.sort()
# print(numbers)
#
# numbers.sort(reverse=True)
# print(numbers)
#
# print(sorted(numbers))
# print(sorted(numbers,reverse=True))
#
# print(numbers[::])
#
# #for loop
# for item in numbers:
#     print(item,end=" ")
#
#
# for item in enumerate(numbers):
#     print(item,end=" ")
#
# str ="hello"
# for ch in str:
#     print(ch,end=" ")

################ chat gpt########################

# duplicate elemnt from list withou using loop or set

my_list = [4, 1, 2, 1, 3, 4, 5, 2, 4]
dic = dict.fromkeys(my_list)
unique = list(dic.keys())
print(unique)

# max and min
sorted_list = sorted(my_list)
print(sorted_list)
print("min = ", sorted_list[0])
print("max = ", sorted_list[-1])

# reverse string using loop

string = "abuthalib"
rev_str = string[::-1]
print(rev_str)

# palindrome or not

# stri=input("enter the straing : ")
stri = "hello"
is_palindrome = stri == stri[::-1]
print(is_palindrome)

# nested list into a single list
nested = [[1, 2], [3, 4, 5], [6, 7]]

new_list = [item for sublist in nested for item in sublist]
print(new_list)

# with out list comperhension

flat = []
for sublist in nested:
    for item in sublist:
        flat.append(item)

print(flat)

# reversig the order of word
my_str = "hello world"
rev = " ".join(my_str.split()[::-1])
print(rev)

# cnvrt list of int into binary
list5 = [1, 2, 3, 4]
bnr = "".join([bin(num)[2::] for num in list5])
print(bnr)

a =10
print(bin(10))