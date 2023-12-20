arr = [1, 2, 3, 4, 5,6,9,7,10,9,7,6,9,10]
first_max = -999999
second_max = -999999
for num in arr:
     if num > first_max:
         second_max = first_max
         first_max = num
     if num > second_max and num != first_max:
         second_max = num

print(second_max)
