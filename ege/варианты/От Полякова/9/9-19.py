m = [0]*300
for i in range(1, 300):
    if i//2 <= 25:
        m[i] = 1
print("---19---")
for n in range(10, 300):
    if m[n] == 0 and (m[n-2] > 0 and m[n-3] > 0 and m[n//2] > 0):
        m[n] = -1
for n in range(10, 300):
    if m[n] == -1:
        print(n)
print("---20---")
for n in range(10, 300):
    if m[n] == 0 and (m[n-2] < 0 or m[n-3] < 0 or m[n//2] < 0):
        m[n] = 2
for n in range(10, 300):
    if m[n] == 2:
        print(n)
print("---21---")
for n in range(10, 300):
    if m[n] == 0 and (m[n-2] > 0 and m[n-3] > 0 and m[n//2] > 0):
        m[n] = -2
for n in range(10, 300):
    if m[n] == -12:
        print(n)