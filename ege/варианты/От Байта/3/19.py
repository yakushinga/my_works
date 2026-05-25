m = [0]*100
for s in range(1, 100):
    if s*2 >= 100:
        m[s] = 1

for s in range(1, 100):
    if m[s] == 0 and (m[s+2] > 0 and m[s+4] > 0 and m[s*2] > 0):
        m[s] = -1
print("---19---")
for s in range(1, 100):
    if m[s] == -1:
        print(s)

for s in range(1, 100):
    if m[s] == 0 and (m[s+2] < 0 or m[s+4] < 0 or m[s*2] < 0):
        m[s] = 2
print("---20---")
for s in range(1, 100):
    if m[s] == 2:
        print(s)

for s in range(1, 100):
    if m[s] == 0 and (m[s+2] > 0 and m[s+4] > 0 and m[s*2] > 0):
        m[s] = -2
print("---21---")
for s in range(1, 100):
    if m[s] == -2:
        print(s)