def f(x, y, w, z):
    return (y <= x) and not(z) and  w
a = [0, 1]
print("x y w z")
for x in a:
    for y in a:
        for w in a:
            for z in a:
                if f(x, y, w, z):
                    print(x, y, w, z)