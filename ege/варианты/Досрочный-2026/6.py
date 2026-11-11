from math import *
k = 0
for x in range(-100, 100):
    for y in range(-100, 100):
        if y > -x and y < -x + 6 and x < 0 and x > -6*sqrt(2):
            print(x, y)
            k += 1
print(k)