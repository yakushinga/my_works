with open ("24_29922.txt") as f:
    s = f.read()

p = []
for i in range(len(s)):
    if s[i] == "Z":
        p.append(i)

lmax = 0
for i in range(len(p)-121):
    l = s[(p[i]+1):p[i+121]]
    if l.count("2026") >= 210:
        lmax = max(len(l), lmax)
print(lmax)