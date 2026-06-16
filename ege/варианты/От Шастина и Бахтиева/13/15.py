A = [0]*41
for i in range(10, 51):
    A[i-10] = i

def mnozhdel(n):
    m = []
    i = 2
    while i*i <= n:
        if n%i == 0:
            m.append(i)
            m.append(n//i)
        i += 1
    return m
B = mnozhdel(481)

for y in range(2, 1000000):
    C = mnozhdel(y)
    flag = True
    if len(C) > 0:
        for x in range(1, 1000000):
            if not((not(x in B)and(x in A)) or not(x in C)):
                flag = False
                break
    else:
        flag = False
    if flag:
        print(y, C)