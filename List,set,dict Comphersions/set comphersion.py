s = set([1,2,3,4,5,6,3,2])

#find odd from this set
odd ={i for i in s if i%2==1}
print(odd)

# square of set
sq = {i*i for i in s}
print(sq)