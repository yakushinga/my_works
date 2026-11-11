ans = []
for m in range(10**6):
    s = str(m)
    for i in range(1, 5):
        if len(s) == 1:
            n = s[0] + "54321"
        elif i > len(s) - 1:
            n  = s[0] + "54" + s[1:] + "321"
        else:
            n = s[0] + "54" + s[1:i] + "32" + s[i:] + "1"
        n = int(n, 10)
        if n%7863 == 0 and not(n in ans) and len(str(n)) <= 9:
            ans.append([n, sum(map(int, str(n)))])
ans.sort(key = lambda x: (x[1], x[0]))
print(*ans)