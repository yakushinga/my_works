def y(t, m, f, g):
    return g and ((t <= m) == f)
a = [False, True]
print("t m f g")
for t in a:
    for m in a:
        for f in a:
            for g in a:
                if y(t, m, f, g):
                    print(int(t), int(m), int(f), int(g))