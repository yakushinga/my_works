with open("24_25361.txt") as f:
    s = f.read()

for sym in "02468":
    s = s.replace(sym, "&")
s = s.split("&")
maxl = 0
for l in s:
    while l.count("F") > 76:
        l = l[:-1]
    if l.count("F") == 76:
        maxl = max(maxl, len(l))
print(maxl + 1)