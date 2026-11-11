N = 2000
from math import ceil
m = [[0]*N for i in range(N)]

for s1 in range(N):
    for s2 in range(N):
        if min(s1+s2-6, ceil(s2/2)+s1, ceil(s1/2)+s2) <= 200:
            m[s1][s2] = 1
m1 = m
for s1 in range(N):
    for s2 in range(N):
        if m1[s1][s2]==0 and (m1[s1-3][s2-3] > 0 or m1[s1//2][s2] > 0 or m1[s1][s2//2] > 0):
            m1[s1][s2] = -1
o19 = []
print("---19---")
for s2 in range(N):
    if m1[76][s2] == -1:
        o19.append(s2)
print(min(o19))

for s1 in range(N):
    for s2 in range(N):
        if m[s1][s2]==0 and (m[s1-3][s2-3] > 0 and m[s1//2][s2] > 0 and m[s1][s2//2] > 0):
            m[s1][s2] = -1

for s1 in range(N):
    for s2 in range(N):
        if m[s1][s2]==0 and (m[s1-3][s2-3] < 0 or m[s1//2][s2] < 0 or m[s1][s2//2] < 0):
            m[s1][s2] = 2

print("---20---")
o20 = []
for s2 in range(N):
    if m1[76][s2] == 2:
        o20.append(s2)
print(min(o20), max(o20))

for s1 in range(N):
    for s2 in range(N):
        if m[s1][s2]==0 and (m[s1-3][s2-3] > 0 and m[s1//2][s2] > 0 and m[s1][s2//2] > 0):
            m[s1][s2] = -2

print("---21---")
o21 = []
for s2 in range(N):
    if m1[76][s2] == -2:
        o21.append(s2)
print(min(o21), max(o21))