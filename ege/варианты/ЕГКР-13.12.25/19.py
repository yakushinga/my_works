m = [0]*125
for s in range(1, 125):
    if s*2 >= 125:
        m[s] = 1

for s in range(1, 125):
    if m[s] == 0 and (m[s+2] > 0 and m[s+4] > 0 and m[s*2] > 0):
        m[s] = -1

print("---19---")
for s in range(1, 125):
    if m[s] == -1:
        print(s)

for s in range(1, 125):
    if m[s] == 0 and (m[s+2] < 0 or m[s+4] < 0 or m[s*2] < 0):
        m[s] = 2

print("---20---")
for s in range(1, 125):
    if m[s] == 2:
        print(s)

for s in range(1, 125):
    if m[s] == 0 and (m[s+2] > 0 and m[s+4] > 0 and m[s*2] > 0):
        m[s] = -2

print("---21---")
for s in range(1, 125):
    if m[s] == -2:
        print(s)