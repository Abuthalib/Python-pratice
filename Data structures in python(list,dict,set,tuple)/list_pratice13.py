# duplicate elemnt from list withou using loop or set
my_list = [1, 2, 3, 4, 23, 8, 5, 9, 43, 54, 12, 56, 23, 12, 1, 3, 5, 6, 9, 10]
dic = dict.fromkeys((my_list))
unique = list(dic.keys())
print(unique)

# max and min
sorted_list = sorted(unique)
print(sorted_list)
print("min = ",sorted_list[0])
print("max = ",sorted_list[-1])

# palindrome or not
s = "Malayalam"
is_palindrome = s ==s[::-1]
if is_palindrome:
    print(s,"is palindrome")
else:
    print(s,"its not palindrome")

# nested list into a single list
nested = [[1,2],[3,4,5],[6,7]]
new =[item for sublist in nested for item in sublist]
print(new)

# reversig the order of word
st = "Good morning abu"
rev = " ".join(st.split()[::-1])
print(rev)