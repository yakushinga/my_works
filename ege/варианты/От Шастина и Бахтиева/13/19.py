from math import ceil
m = [0]*5000
for s in range(0, 5000):
    if ceil(s/2) <= 47:
        m[s] = 1
for s in range(0, 5000):
    if m[s] == 0 and (m[s-3] > 0 and m[s-5] > 0 and m[ceil(s/2)] > 0):
        m[s] = -1
print("---19----")
for s in range(0, 5000):
    if m[s] == -1:
        print(s)

for s in range(0, 5000):
    if m[s] == 0 and (m[s-3] < 0 or m[s-5] < 0 or m[ceil(s/2)] < 0):
        m[s] = 2
print("---20----")
for s in range(0, 5000):
    if m[s] == 2:
        print(s)

for s in range(0, 5000):
    if m[s] == 0 and (m[s-3] > 0 and m[s-5] > 0 and m[ceil(s/2)] > 0):
        m[s] = -2
print("---21----")
for s in range(0, 5000):
    if m[s] == -2:
        print(s)