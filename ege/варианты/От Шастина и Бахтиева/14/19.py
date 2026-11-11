m = [[0]*809 for i in range(809)]

for s1 in range(809):
    for s2 in range(809):
        if max(s1, s2)*2 + min(s1, s2) >= 808:
            m[s1][s2] = 1

for s1 in range(809):
    for s2 in range(809):
        if m[s1][s2] == 0 and(m[s1*2][s2] > 0 and m[s1][s2*2] > 0 and m[s1+3][s2] > 0 and m[s1][s2+3] > 0 ):
            m[s1][s2] = -1
print("---19---")

for s2 in range(809):
    if m[36][s2] == -1:
        print(s2)

for s1 in range(809):
    for s2 in range(809):
        if m[s1][s2] == 0 and(m[s1*2][s2] < 0 or m[s1][s2*2] < 0 or m[s1+3][s2] < 0 or m[s1][s2+3] < 0):
            m[s1][s2] = 2
print("---20---")

for s2 in range(809):
    if m[36][s2] == 2:
        print(s2)

for s1 in range(809):
    for s2 in range(809):
        if m[s1][s2] == 0 and(m[s1*2][s2] > 0 and m[s1][s2*2] > 0 and m[s1+3][s2] > 0 and m[s1][s2+3] > 0 ):
            m[s1][s2] = -2
print("---21---")

for s2 in range(809):
    if m[36][s2] == -2:
        print(s2)