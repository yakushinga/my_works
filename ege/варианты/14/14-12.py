def q1(s, i):
    if i < 0:
        return s
    return q3(s, i-1)
def q2(s, i):
    if i < 0:
        return s
    if s[i] == "0":
        s = s[:i] + "1" + s[i+1:]
        return q3(s, i-1)
    else:
        s = s[:i] + "0" + s[i+1:]
        return q1(s, i-1)
def q3(s, i):
    if i < 0:
        return s
    return q2(s, i-1)
print(q1("1"*221, 220).count("1"))
print(bin(161)[2:])