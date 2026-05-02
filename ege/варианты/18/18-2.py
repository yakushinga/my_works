def f(x, y, z, w):
    return (x and not(y)) or (x == z) or w
a = [0, 1]
for x in a:
    for y in a:
        for z in a:
            for w in a:
                if not(f(x, y, z, w)):
                    print(x, y, z, w)