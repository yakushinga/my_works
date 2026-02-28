from math import *
def f(x, y):
    if x<0 and x>-6 and y < sqrt(3)*x and y > sqrt(3)*x -6:
        return True
k = 0
for x in range(-200, 1):
    for y in range(-200, 1):
        if f(x, y):
            k += 1
print(k)