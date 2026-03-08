m = [0]*3000
for n in range (1, 3000):
    if n//3 <= 40:
        m[n] = 1
print("---19---")
for n in range(1, 3000):
    if m[n] == 0 and m[n-2] > 0 and m[n-4] > 0 and m[n//3] > 0:
        m[n] = -1
for n in range(1, 3000):
    if m[n] == -1:
        print(n)

print("---20---")
for n in range(1, 3000):
    if m[n] == 0 and (m[n-2] < 0 or m[n-4] < 0 or m[n//3] < 0):
        m[n] = 2
for n in range(1, 3000):
    if m[n] == 2:
        print(n)

print("---21---")
for n in range(1, 3000):
    if m[n] == 0 and (m[n-2] > 0 and m[n-4] > 0 and m[n//3] > 0):
        m[n] = -2
for n in range(1, 3000):
    if m[n] == -2:
        print(n)