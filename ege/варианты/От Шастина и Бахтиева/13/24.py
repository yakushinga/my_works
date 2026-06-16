alf = "0123456789ABCDEF"
nonalf = "GHIJKLMNOPQRSTUVWXYZ"
with open("24_29924.txt") as f:
    s = f.read()

for cif in nonalf:
    s = s.replace(cif, "G")

p = []
for i in range(len(s)):
    if alf.find(s[i])%2 == 0:
        p.append(i)
print(len(p))
flag = False
for j in range(len(p)-259):
    l = s[p[j]:p[j+259]+1]
    if l.count("G") == 0:
        if not(flag):
            flag = True
            minn = l
        else:
            if int(l, 16) < int(minn, 16):
                minn = l
print(len(minn)-1)