with open("17_29839.txt") as f:
    c = list(map(int, f.read().split()))
max37 = -100001
for el in c:
    if abs(el)%100 == 37 and el > max37:
        max37 = el

ans = []
for i in range(len(c) - 3):
    k = 0
    for j in range(i, i+3):
        if abs(c[j]) >= 100 and abs(c[j]) < 1000:
            k += 1
    sr = sum(c[i:i+3])/3
    if k == 2 and sr > 0 and sr < max37:
        ans.append(sum(c[i:i+3]))
print(len(ans), max(ans))