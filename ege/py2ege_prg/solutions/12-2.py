with open ("/home/user/repo/ege/py2ege_prg/12/data/data12-2.txt") as f:
    m, k, n = f.readline().split()
    m, k, n = int(m), int(k), int(n)
    a = []
    for i in range (n):
        p1, p2 = f.readline().split()
        p1, p2 = int(p1), int(p2)
        a.append((p1, p2))
a.sort()
print(a)
b = [0]*k
