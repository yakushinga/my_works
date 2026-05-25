ans = []
for n in range(1, 10**6):
    for i in range(0,len(str(n))+1):
        l = str(n)
        m = int(l[0] + "13" + l[1:i] + "79" + l[i:] + "9", 10)
        if m%7521 == 0 and not(m in ans) and len(str(m)) <= 9:
            ans.append([m, sum(map(int, str(m)))])
ans.sort(key = lambda x: (x[1], x[0]))
print(ans)