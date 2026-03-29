def q3(s, i):
    if i >= len(s):
        return s
    if s[i] == "0":
        return q2(s, i + 1)
    if s[i] == "1":
        return q1(s, i + 1)

def q2(s, i):
    if i >= len(s):
        return s
    if s[i] == "0":
        s = s[:i] + "1" + s[i+1:]
        return q3(s, i + 1)
    if s[i] == "1":
        s = s[:i] + "0" + s[i+1:]
        return q3(s, i + 1)

def q1(s, i):
    if i >= len(s):
        return s
    return q2(s, i + 1)

print(q1("1"*30 + "0"*45, 0), q1("1"*30 + "0"*45, 0).count("1"))
