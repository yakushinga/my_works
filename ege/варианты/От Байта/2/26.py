with open("26_22168.txt") as f:
    n = int(f.readline())
    r = []
    for s in f:
        r.append(list(map(int, s.split())))
r.sort()

st = []
sti = [229, 0]
for i in range(1, len(r)):
    if r[i][0] == sti[0]:
        if r[i][1]%2 == 0:
            sti[1] += 1
    else:
        st.append(sti)
        sti = [r[i][0], 0]
        if r[i][1]%2 == 0:
            sti[1] += 1
st.sort(key = lambda x: (-x[1], x[0]))
print(st[0])
