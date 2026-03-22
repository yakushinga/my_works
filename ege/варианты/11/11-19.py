d = [0]*700
for s in range(700):
    if s//3 <= 19:
        d[s] = 1
for s in range(700):
    if d[s] == 0 and (d[s//3] > 0 and d[s-2] > 0 and d[s-5] > 0):
        d[s] = -1
print("---19---")
for s in range(700):
    if d[s] == -1:
        print(s, end = " ")
print()

for s in range(700):
    if d[s] == 0 and (d[s//3] < 0 or d[s-2] < 0 or d[s-5] < 0):
        d[s] = 2
print("---20---")
for s in range(700):
    if d[s] == 2:
        print(s, end = " ")
print()

for s in range(700):
    if d[s] == 0 and (d[s//3] > 0 and d[s-2] > 0 and d[s-5] > 0):
        d[s] = -2
print("---21---")
for s in range(700):
    if d[s] == -2:
        print(s, end = " ")
print()