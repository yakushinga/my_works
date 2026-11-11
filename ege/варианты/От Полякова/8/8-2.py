a = [0,1]
def f(x,y,w,z):
    return int((not(x) and y and z and not(w)) or (not(x) and y and not(z) and not(w)) or (x and y and z and not(w)))
print("x y w z F")
for x in a:
    for y in a:
        for w in a:
            for z in a:
                print(x, y, w, z, f(x, y, w, z))