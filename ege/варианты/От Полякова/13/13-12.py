def q1(s, i):
    if i == -1:
        return s
    return q2(s, i-1)
def q2(s, i):
    if i == -1:
        return s
    if s[i] == "0":
        s = s[:i] + "1" + s[i+1:]
    else:
        s = s[:i] + "0" + s[i + 1:]
    return q3(s, i-1)
def q3(s, i):
    if i == -1:
        return s
    return q1(s, i-1)
print(q1("0"*12 + "1"*15, 26).count("0"))
