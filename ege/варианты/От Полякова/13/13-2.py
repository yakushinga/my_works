# (x → (z ≡ w)) ˅ ¬(y → w)
def f(x, y, w, z):
    return (x <= (z == w)) or not(y <= w)
a = [0, 1]
print("x y w z")
for x in a:
    for y in a:
        for w in a:
            for z in a:
                if not(f(x, y, w, z)):
                    print(x, y, w, z)