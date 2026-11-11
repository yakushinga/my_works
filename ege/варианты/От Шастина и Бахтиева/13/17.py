with open("17_29840.txt") as f:
    s = list(map(int, f.read().split()))
k119 = 0
for el in s:
    if el < 0 and abs(el)%119 == 0:
        k119 += 1
ans = []
for i in range(len(s) - 1):
    if s[i] + s[i+1] < k119:
        ans.append(s[i] + s[i+1])
print(len(ans), min(ans))