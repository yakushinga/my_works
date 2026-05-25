def f(s):
    for i in range (1, len(s)):
        if int(s[i])%2 == int(s[i-1])%2:
            return False
    return True
for n in range(10015, 100000, 15):
    if f(str(n)):
        print(n)
