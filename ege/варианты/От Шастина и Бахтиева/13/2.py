def f(x, y, z, w):
    return (y and not(w) and z) or (y and not(w) and not(x))
a = [0, 1]
for x in a:
    for y in a:
        for z in a:
            for w in a:
                if f(x, y, z, w):
                    print(x, y, z, w)