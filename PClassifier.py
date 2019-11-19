from builtins import print
from Point import Point

import numpy as np
import math

# read file, build Points list ---------------------------------------

file = open('ML_hw2_data.txt', 'r')

lines = file.readlines()

list_of_points = []
for line in lines:
    point = Point(line.strip())
    list_of_points.append(point)

print("list of all points:")
for item in list_of_points:
    print(item)
print()

# build lists for numbers in 0 class and 1 class ---------------------

numbers_0 = []
numbers_1 = []
for point in list_of_points:
    if point.class_of_point == 0:
        numbers_0.append(point.x)
    else:
        numbers_1.append(point.x)

print(0)
for number in numbers_0:
    print(number)
print()

print(1)
for number in numbers_1:
    print(number)
print()

# mean, stddev, varyans for 0 and 1 ------------------------------------

nd_array_0 = np.array(numbers_0)
nd_array_1 = np.array(numbers_1)

mean_0 = nd_array_0.mean()
stddev_0 = nd_array_0.std()
variance_0 = nd_array_0.var()

mean_1 = nd_array_1.mean()
stddev_1 = nd_array_1.std()
variance_1 = nd_array_1.var()

# calculate the g function, 4.28 in book, section 4.5 -----------------
# and predict the class -----------------------------------------------

X = 1.2
X = 3.0
X = 5.0

g_for_0 = - math.log(stddev_0) - (((X - mean_0)**2) / (2*variance_0))
g_for_1 = - math.log(stddev_1) - (((X - mean_1)**2) / (2*variance_1))

if g_for_0 > g_for_1:
    print("answer class is 0")
else:
    print("answer class is 1")

