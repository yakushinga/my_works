ans = []
for n1 in range(-1, 10):
    for n2 in range(10):
        for n3 in range(-1, 10):
            for n4 in range(10):
                if n1 == -1:
                    l1 = ""
                else:
                    l1 = str(n1)
                l2 = str(n2)
                if n3 == -1:
                    l3 = ""
                else:
                    l3 = str(n3)
                l4 = str(n4)
                s = "21" + l1 + "93" + l2 + "3" + l3 + "5" + l4 + "2"
                if len(s) <= 10:
                    n = int(s)
                    if n%2026 == 0:
                        ans.append([n, n//2026])
ans.sort()
print(ans)