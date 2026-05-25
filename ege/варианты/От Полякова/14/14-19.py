m = [0]*58
for s in range(1, 58):
    if s*2 >= 58:
        m[s] = 1

for s in range(1, 58):
    if m[s] == 0 and (m[s+1] > 0 and m[s+4] > 0 and m[s*2] > 0):
        m[s] = -1

print("---19---")
for s in range(1, 58):
    if m[s] == -1:
        print(s)

for s in range(1, 58):
    if m[s] == 0 and (m[s+1] < 0 or m[s+4] < 0 or m[s*2] < 0):
        m[s] = 2

print("---20---")
for s in range(1, 58):
    if m[s] == 2:
        print(s)

for s in range(1, 58):
    if m[s] == 0 and (m[s+1] > 0 and m[s+4] > 0 and m[s*2] > 0):
        m[s] = -2

print("---21---")
for s in range(1, 58):
    if m[s] == -2:
        print(s)
print(m)