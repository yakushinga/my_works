with open("26_30474.txt") as f:
    n = int(f.readline())
    t = []
    for i in range(n):
        t.append(list(map(int, f.readline().split())))
z = [0]*1441
for time in t:
    for i in range(time[0], time[1]):
        z[i] += 1
print(max(z))
k = 0
for el in z:
    if el == max(z):
        k += 1
print(k)