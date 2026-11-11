def f(x, y, z, w):
    return (x <= w) and ((w == y) or (y <= z))
a = [0, 1]
for x in a:
    for y in a:
        for z in a:
            for w in a:
                print(x, y, z, w, int(f(x, y, z, w)))