with open("17-418.txt") as f:
    m = list(map(int, f.read().split()))
min1 = 10000
min2 = 10000
for n in m:
    if n >= 6**3 and n < 6**4 and n < min1:
        min1 = n
    if n >= 9 ** 2 and n < 9 ** 3 and n < min2:
        min2 = n
o1 = min1%5
o2 = min2%13
ans = []
for i in range(len(m)-1):
    k1 = 0
    k2 = 0
    for j in range(i, i + 2):
        if m[j] % 11 == o1:
            k1 += 1
        if m[j] % 7 == o2:
            k2 += 1
    if k1 >= 1 and k2 >= 1:
        ans.append(sum(m[i:i+2]))
print(len(ans), max(ans))