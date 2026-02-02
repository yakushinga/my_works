s = open("24-356.txt").read()
alf = "0123456789ABC"
i = 0
m = []
while i < len(s):
    sl = ""
    while s[i] in alf and i < len(s):
        sl += s[i]
        i += 1
    if sl != "": m.append(sl)
    i += 1

b = [int(x, 14) for x in m]
maximum = 0
imax = 0
print(m)
for x in range(len(b)):
    if b[x]%2 == 0 and b[x] > maximum:
        maximum = max(b[x], maximum)
        imax = x
print(maximum)

print(len(m[imax]))