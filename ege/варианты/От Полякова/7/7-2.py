def  F(x, y, w, z):
    return ((w <= y) <= x) or not(z)

a = [0, 1]
print("x y w z F")
for x in a:
    for y in a:
        for w in a:
            for z in a:
                print(x, y, w, z, F(x, y, w, z))