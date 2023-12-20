def double(bonus):
    return bonus *2
bonuses =[100,200,300]
iterators = map(double,bonuses)

print(list(iterators))

# usng lambda
bonuses = [100, 200, 300]
iterators = map(lambda  bonus: bonus*2,bonuses)
print(list(iterators))