with open("24_23975.txt") as f:
    s = f.read()
p = []
for i in range(len(s)):
    if s[i] == "X":
        p.append(i)
maxl = 0
for j in range(1,len(p)-60):
    l = s[p[j-1]+1:p[j+60]]
    if l.count("2026") >= 75:
        maxl = max(p[j+60]-1-p[j-1]-1+1, maxl)
print(maxl)