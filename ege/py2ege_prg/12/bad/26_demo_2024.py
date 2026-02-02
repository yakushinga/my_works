from functools import lru_cache
f = open('i/input_4.txt')
n = int(f.readline())
r = []
for i in f:
    r.append(list(map(int, i.split())))
r.sort()
ans = []
@lru_cache(None)
def p(nk, cnt, time_end, st_end):
    if cnt > 1:
        ans.append([cnt, st_end])
    for i in range(nk + 1, n):
        if r[i][0] >= time_end:
            p(i, cnt + 1, r[i][1], r[i][0] - time_end)
for a in range(n):
    p(a, 1, r[a][1], 0)
ans.sort(reverse = True)
print(ans[0])

