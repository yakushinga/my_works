with open("17_28762.txt") as f:
    c = list(map(int, f.read().split()))
min32 = 1000000000
for el in c:
    if el%23 == 0 and el < min32:
        min32 = el
ans = []
for i in range(len(c) - 1):
    if c[i]%min32 == 0 or c[i+1]%min32 == 0:
        ans.append(sum(c[i:i+2]))
print(len(ans), max(ans))