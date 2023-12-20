n1=set(["abu","meh"])
n2 = set(["meh","jebi"])

names_union = n1.union(n2)

names1 = n1|n2

print(names_union)
print(names1)

name_interstion = n1.intersection(n2)
name1 = n1&n2

print(name_interstion)
print(name1)


names_diff =n1.difference(n2)
name1 =n1-n2

print(names_diff)
print(name1)

skills = set(['Problem solving','Critical Thinking'])
print(skills)
