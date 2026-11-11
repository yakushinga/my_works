def q1(s, i):
    if len(s) == i:
        return s
    if s[i] == "0":
        return q3(s, i + 1)
    return q2(s, i + 1)
def q2(s, i):
    if len(s) == i:
        return s
    if s[i] == "0":
        return q3(s[:i] + "1" + s[i+1:], i + 1)
    return q3(s[:i] + "0" + s[i+1:], i + 1)
def q3(s, i):
    if len(s) == i:
        return s
    return q2(s, i + 1)
print(q1("0"*151, 0).count("1"))
print(bin(193)[2:])