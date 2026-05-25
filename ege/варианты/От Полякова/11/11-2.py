def f(x, y, w, z):
    return ((x <= y) <= z) or not(w)
a = [0, 1]
print("x y w z F")
for x in a:
    for y in a:
        for w in a:
            for z in a:
                if not(f(x, y, w, z)):
                    print(x, y, w, z, 0)