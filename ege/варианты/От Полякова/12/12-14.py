def f(n):
    if n == 0:
        return "0"
    s = ""
    while n:
        s = str(n%5) + s
        n//=5
    return s
for x in range(1, 2030):
    s = f(25**75-x)
    if s.count("1") <= 1:
        print(x, s)
        break
        
