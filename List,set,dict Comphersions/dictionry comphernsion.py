cities = ["delhi", "newyork", "paris"]
countries = ["India", "USA", "France"]

# creating dictionry from this two list
z = zip(countries, cities)
for a in z:
    print(a)

d = {country: city for country, city in zip(countries, cities)}
print(d)
