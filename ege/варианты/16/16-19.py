m = [0]*61
for s in range(1, 61):
    if s*2 >= 61 and s*2 <= 80 or s + 1 >= 61:
        m[s] = 1
print("---19---")
print(m.count(1))
for s in range(1, 61):
    if m[s] == 0 and (s*2 > 80 and m[s+1] > 0 or s*2 <= 80 and m[s*2] > 0 and m[s+1] > 0):
        m[s] = -1
for s in range(1, 61):
    if m[s] == 0 and (s*2 > 80 and m[s+1] < 0 or s*2 <= 80 and (m[s*2] < 0 or m[s+1] < 0)):
        m[s] = 2
print("---20---")
for s in range(1, 61):
    if m[s] == 2:
        print(s)
for s in range(1, 61):
    if m[s] == 0 and (s*2 > 80 and m[s+1] > 0 or s*2 <= 80 and m[s*2] > 0 and m[s+1] > 0):
        m[s] = -2
print("---21---")
for s in range(1, 61):
    if m[s] == -2:
        print(s)
