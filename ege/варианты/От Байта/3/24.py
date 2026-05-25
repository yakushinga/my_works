with open("24_24868.txt") as f:
    s = f.read()
i = 0
maxl = 0
while i < len(s):
    l = 1
    alf = s[i]
    i += 1
    while len(alf) <= 2 and i < len(s):
        if not(s[i] in alf):
            alf += s[i]
        l += 1
        i += 1
    if l > maxl:
        maxl = l
    i += 1
print(maxl)