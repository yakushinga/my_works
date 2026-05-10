def f(x, y, z, w):
    return (x and y and not(z)) or (not(w) and y and z)
a = [0, 1]
for x in a:
    for y in a:
        for z in a:
            for w in a:
                if f(x, y, z, w):
                    print(x, y, z, w)