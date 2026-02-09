# mdf 26-169  https://kpolyakov.spb.ru/school/ege.htm
lines, count = {}, {}
with open('26-169.txt') as f:
    n, *size = map(int, f.readline().split())
    for _ in range(n):
        i = tuple(map(int, f.readline().split()))
        for u in 0, 1:
            z, p = (1 - 2 * u, i[u]), not u
            if z not in lines:
                lines[z] = [0, size[p] + 1]
            lines[z].append(i[p])
        count[i] = 0
[lines[u].sort() for u in lines]
for q, z in lines.items():
    for k in range(1, len(z) - 1):
        i = (q[1], z[k])[::q[0]]
        count[i] += z[k + 1] - z[k - 1] - 2
ans = max(count.items(), key=lambda x: (x[1], x[0][1], x[0][0]))
print(ans[0][0], ans[1])
# для каждого ряда сохраним координаты домов на нем, добавляя фиктивные дома на границе поля.
# отсортируем коорднаты домов в каждом ряду.
# пройдем по всем рядам, и для каждого дома в ряду найдем количество видимых ячеек в обоих направлениях.
# горизонтальные и вертикальные ряды храним в одном словаре.
