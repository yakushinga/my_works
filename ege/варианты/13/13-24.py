with open("24-347.txt") as f:
    s = f.read()
alf = "0123456789ABCDE"
smax = [0, 0]
nonalf = "FGHIJKLMNOPQRSTUVWXYZ"

i = 0
while i < len(s):
    l = ""
    while s[i] in alf and i < len(s):
        l += s[i]
        i += 1
    if l != "":
        n = int(l, 15)
        if n > smax[0]:
            smax = [n, i-2]
    i += 1
print(smax)