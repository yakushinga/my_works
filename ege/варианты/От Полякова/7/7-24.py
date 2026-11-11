from operator import truediv

with open ("24-347.txt") as f:
    c = f.read()

maxs = ""
maxi = -1
flag = False
for i in range(len(c)):
    if not flag and int(c[i],36) > 0 and int(c[i],36) <= 7:
        flag = True
        s = c[i]
        j = i
    elif flag and int(c[i],36) >= 0 and int(c[i],36) <= 7:
        s += c[i]
    elif flag and int(c[i],36) > 7:
        flag = False
        if len(s) > len(maxs):
            maxs = s
            maxi = j
        elif len(s) == len(maxs) and int(s, 8) < int(maxs, 8):
            maxs = s
            maxi = j
print(s,maxi)