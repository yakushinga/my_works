with open("24-347.txt") as f:
    s = f.read()
n = []
alf = "0123456789AB"
i = 0
while i < len(s):
    if s[i] in alf:
        j = i
        i += 1
        while s[i] in alf:
            i += 1
        ni = [i-1, int(s[j:i],12)]
        if ni[1]%11 == 0: n.append(ni)
    i += 1
maxi = 0
for i in range(1, len(n)):
    if n[i][1] > n[maxi][1]:
        maxi = i
print(n[maxi][0])
