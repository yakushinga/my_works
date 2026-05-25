s = open("24-356.txt").read()
alf = "0123456789ABCD"
i = 0
m = []
while i < len(s):
    sl = ""
    flag = 0
    while s[i] in alf and i < len(s):
        if s[i] != '0':
            flag = 1
        if flag == 1:
            sl += s[i]
        i += 1
    if sl != "":
        m.append(sl)
    i += 1

b = []
for x in m:
    b.append(int(x, 14))
maximum = 0
imax = 0
print(len(b), len(m))

for i in range(len(b)):
    if b[i]%2 == 0 and b[i] > maximum:
        maximum = b[i]
        imax = i
print(maximum)

print(len(m[imax]), "\n", m[imax])