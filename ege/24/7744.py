with open("24-303.txt") as f:
    s = f.read()

def f(s):
    pairs = {')':'(', ']':'[', '}':'{'}
    stack = []
    if s[0] not in "([{" or s[-1] not in "}])":
        return False
    for i in range (1, len(s)-1):
        ch = s[i]
        if ch in "([{":
            stack.append(ch)
        elif ch in "})]":
            if not stack or stack[-1] != pairs[ch]:
                return False
            stack.pop()
    return not stack
s1 = []
s2 = []
s3 = []
s11 = []
s21 = []
s31 = []

for i in range(len(s)):
    if s[i] == "[":
        s1.append(i)
    if s[i] == "(":
        s2.append(i)
    if s[i] == "]":
        s11.append(i)
    if s[i] == ")":
        s21.append(i)
    if s[i] == "{":
        s3.append(i)
    if s[i] == "}":
        s31.append(i)
nmax = 0
for i in s1:
    for j in s11:
        if j > i:
            if f(s[i:j+1]):
                print(s[i:j+1])
                nmax = max(j - i + 1, nmax)
for i in s2:
    for j in s21:
        if j > i:
            if f(s[i:j+1]):
                print(s[i:j+1])
                nmax = max(j - i + 1, nmax)
for i in s3:
    for j in s31:
        if j > i:
            if f(s[i:j+1]):
                print(s[i:j+1])
                nmax = max(j - i + 1, nmax)
print(nmax)