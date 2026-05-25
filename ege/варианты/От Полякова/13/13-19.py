m = [0]*39
for s in range(1, 39):
    if s*2 >= 39:
        m[s] = 1
for s in range(1, 39):
    if m[s] == 0 and (m[s+1] > 0 and m[s+3] > 0 and m[s*2] > 0):
        m[s] = -1
print ("---19---")
for s in range(1, 39):
    if m[s] == -1:
        print(s)

for s in range(1, 39):
    if m[s] == 0 and (m[s+1] < 0 or m[s+3] < 0 or m[s*2] < 0):
        m[s] = 2
print ("---20---")
for s in range(1, 39):
    if m[s] == 2:
        print(s)

for s in range(1, 39):
    if m[s] == 0 and (m[s+1] > 0 and m[s+3] > 0 and m[s*2] > 0):
        m[s] = -2
print ("---21---")
for s in range(1, 39):
    if m[s] == -2:
        print(s)