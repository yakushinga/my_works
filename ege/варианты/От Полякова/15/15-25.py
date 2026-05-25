ans = []
for n in range(1, 10000):
    for i in range(1, len(str(n))+1):
        s = str(n)
        m = int(s[0] + "05" + s[1:i] + "22" + s[i:] + "3", 10)
        if m % 8587 == 0 and not([m, sum(map(int, str(m)))] in ans):
            ans.append([m, sum(map(int, str(m)))])
ans.sort(key=lambda x: (x[1], x[0]))
print(ans)