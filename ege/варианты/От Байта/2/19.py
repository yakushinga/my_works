m = [0]*5000
for s in range(1, 5000):
    if s//4 <= 20:
        m[s] = 1

for s in range(1, 5000):
    if m[s] == 0 and (m[s-5] > 0 and m[s-7] > 0 and m[s//4] > 0):
        m[s] = -1
print("---19---")
for s in range(1, 5000):
    if m[s] == -1:
        print(s)

for s in range(1, 5000):
    if m[s] == 0 and (m[s - 5] < 0 or m[s - 7] < 0 or m[s // 4] < 0):
        m[s] = 2
print("---20---")
for s in range(1, 5000):
    if m[s] == 2:
        print(s)

for s in range(1, 5000):
    if m[s] == 0 and (m[s-5] > 0 and m[s-7] > 0 and m[s//4] > 0):
        m[s] = -2
print("---21---")
for s in range(1, 5000):
    if m[s] == -2:
        print(s)