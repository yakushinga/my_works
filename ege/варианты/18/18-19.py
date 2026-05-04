m = [0]*31
for s in range(1, 31):
    if s-3 <= 0 or s//2 <= 0:
        m[s] = 1
for s in range(1, 31):
    if m[s] == 0 and (m[s-2] > 0 and m[s-3] > 0 and m[s//2] > 0):
        m[s] = -1
print("---19---")
for s in range(1, 31):
    if m[s] == -1:
        print(s)
for s in range(1, 31):
    if m[s] == 0 and (m[s-2] < 0 or m[s-3] < 0 or m[s//2] < 0):
        m[s] = 2
print("---20---")
for s in range(1, 31):
    if m[s] == 2:
        print(s)
for s in range(1, 31):
    if m[s] == 0 and (m[s-2] > 0 and m[s-3] > 0 and m[s//2] > 0):
        m[s] = -2
print("---21---")
for s in range(1, 31):
    if m[s] == -2:
        print(s)