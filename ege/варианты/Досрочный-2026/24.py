with open("24_28765.txt") as f:
    s = f.read()
p = []
for i in range(len(s)-1):
    if s[i:i+2] == "BC":
        p.append(i)
maxl = 0
for i in range(len(p)-181):
    maxl = max(maxl, p[i+181]-p[i]-1+1)
print(maxl)