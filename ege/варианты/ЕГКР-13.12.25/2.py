def f(w, x, y, z):
    return (w == z) or not(y <= w) or not(x)
a = [0, 1]
for w in a:
    for x in a:
        for y in a:
            for z in a:
                if not(f(w, x, y, z)):
                    print(w, x, y, z)
