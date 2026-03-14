def f(x, y, w, z):
    return (y <= int(not((x <= z)))) or w
a = [0,1]
for x in a:
    for y in a:
        for w in a:
            for z in a:
                if not(f(x, y, w, z)):
                    print(x, y, w, z)