def f(x, y, z, w):
    return (not(y) and (w <= z)) and ((w == x) or (int((y and z)) == x))

a = [0, 1]
print("x y z w")
for x in a:
    for y in a:
        for z in a:
            for w in a:
                if f(x, y, z, w):
                    print(x, y, z, w)