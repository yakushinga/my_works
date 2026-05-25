with open("24-347.txt") as f:
    s = f.read()
alf = "0123456789ABCD"
i = 0
n = [0, 0]
while i  < len(s):
    if s[i] in alf:
        j = i
        while s[i] in alf:
            i += 1
        ni = int(s[j:i], 14)
        if ni % 5 == 0:
            if ni > n[0]:
                n = [ni, j]
    i += 1
print(n)

