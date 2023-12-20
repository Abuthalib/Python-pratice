# Python program to check if two
# to get unique values from list
# using numpy.unique

import numpy as np


def unique(list1):
    x = np.array(list1)
    print(np.unique(x))


list1 = [10, 35, 20, 10, 2, 6, 2, 7, 7, 20]
unique(list1)

s = set(list1)
print(s)
