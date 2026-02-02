"""
(Статград-2022) Текстовый файл data11-8.txt состоит не более чем из 10^6
заглавных буквы латинского алфавита (ABC…Z). Определите максимальное количество
идущих подряд символов, среди которых не более одной буквы D.
(Ответ: 182)
"""
target = 'D'

with open("i/data11-8.txt") as F:
  s = target + F.readline() + target

T = []
for i in range(len(s)):
  if s[i] == target:
    T.append( i )

ma = 0
for i in range(2,len(T)):
  ma = max(ma, T[i] - T[i-2] - 1)

print( target, ma )




