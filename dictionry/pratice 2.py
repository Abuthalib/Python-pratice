# duplicate elemnt from list withou using loop or set
my_list =[4,5,6,78,2,4,5,1,5,1,9,43,56,21,1]
dic = dict.fromkeys(my_list)
unique = list(dic.keys())
print(unique)

# max and min
sorted_list = sorted(my_list)
print(sorted_list)
print("min = ",sorted_list[0])
print("max = ",sorted_list[-1])

# reverse string using loop
string = "oyo"
rev_str = string[::-1]
print(rev_str)

# palindrome or not
s= "malayalam"
is_palindrom  = s == s[::-1]
if is_palindrom:
    print(s," is palindrome")
else:
    print(s,"its not palindrome")

# nested list into a single list
nested = [[1, 2], [3, 4, 5], [6, 7]]
new_l =[item for sublist in nested for item in sublist]
print(new_l)

# with out list comperhension

flat =[]
for sublist in nested:
    for item in sublist:
        flat.append(item)
print(flat)

# reversig the order of word
my_str = "good morining abuthalib"
rev = " ".join(my_str.split()[::-1])
print(rev)

# cnvrt list of int into binary
list3 =[1,2,3,4]
bnr = "".join([bin(num)[2::]for num in list3])
print(bnr)