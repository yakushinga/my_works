m = [[0]*65 for i in range(65)]

for s1 in range(1, 65):
    for s2 in range(1, 65):
        if max(s1, s2)*3 + min(s1, s2) >= 65:
            m[s1][s2] = 1
for s1 in range(1, 65):
    for s2 in range(1, 65):
        if m[s1][s2] == 0 and (m[s1*3][s2] > 0 and m[s1][s2*3] > 0 and m[s1+1][s2] > 0 and m[s1][s2+1] > 0):
            m[s1][s2] = -1
print("---19---")
for s2 in range(1, 65):
    if m[6][s2] == -1:
        print(s2)

for s1 in range(1, 65):
    for s2 in range(1, 65):
        if m[s1][s2] == 0 and (m[s1*3][s2] < 0 or m[s1][s2*3] < 0 or m[s1+1][s2] < 0 or m[s1][s2+1] < 0):
            m[s1][s2] = 2
print("---20---")
for s2 in range(1, 65):
    if m[6][s2] == 2:
        print(s2)

for s1 in range(1, 65):
    for s2 in range(1, 65):
        if m[s1][s2] == 0 and (m[s1*3][s2] > 0 and m[s1][s2*3] > 0 and m[s1+1][s2] > 0 and m[s1][s2+1] > 0):
            m[s1][s2] = -2
print("---21---")
for s2 in range(1, 65):
    if m[6][s2] == -2:
        print(s2)