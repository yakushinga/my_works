m = [0]*5001
for s in range(1, 5001):
    if s//3 <= 25:
        m[s] = 1

for s in range(1, 5001):
    if m[s] == 0 and (m[s-4] > 0 and m[s-6] > 0 and m[s//3] > 0):
        m[s] = -1
print("---19---")
for s in range(1, 5001):
    if m[s] == -1:
        print(s)

for s in range(1, 5001):
    if m[s] == 0 and (m[s-4] < 0 or m[s-6] < 0 or m[s//3] < 0):
        m[s] = 2
print("---20---")
for s in range(1, 5001):
    if m[s] == 2:
        print(s)

for s in range(1, 5001):
    if m[s] == 0 and (m[s-4] > 0 and m[s-6] > 0 and m[s//3] > 0):
        m[s] = -2
print("---21---")
for s in range(1, 5001):
    if m[s] == -2:
        print(s)