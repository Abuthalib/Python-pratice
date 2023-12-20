my_dict = {'apple': 50, 'banana': 20, 'orange': 80, 'grapes': 30}

max_key = None
max_value = float('-inf')

for key, value in my_dict.items():
    if value > max_value:
        max_value = value
        max_key = key

print("Key with maximum value:", max_key)
