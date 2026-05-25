def f(x, y, w, z):
    return not(x <= z) or y == w or y
a = [0,1]
print("x y w z F")
for x in a:
    for y in a:
        for w in a:
            for z in a:
                if int(f(x, y, w, z)) == 0:
                    print(x, y, w, z, int(f(x, y, w, z)))
