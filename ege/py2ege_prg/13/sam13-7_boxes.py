"""
В магазине для упаковки подарков есть N кубических коробок разной стоимости.
Самой интересной считается упаковка подарка по принципу матрёшки: подарок
упаковывается в одну из коробок, та в свою очередь в другую коробку и т. д.
Одну коробку можно поместить в другую, если длина её сто-роны хотя бы на
K единиц меньше длины стороны другой ко-робки. Определите наибольшее количество
коробок, которое можно использовать для упаковки одного подарка, так чтобы
стоимость упаковки не превысила M единиц, и минимальную возможную итоговую
стоимость этой упаковки. Размер подарка позволяет поместить его в самую
маленькую коробку. В первой строке файла data13-6.txt записаны натуральные ч
исла N – количество коробок в магазине, K – минимально допустимая разница длин
сторон соседних коробок в матрёшке, и M – максимально допустимая стоимость
упаковки. В каждой из следующих N строк записана длина стороны очередной
коробки и через пробел – стоимость коробки.

Ответ: 138 4976
"""

# Автор: А. Кабанов

from math import isinf
with open("data/data13-7.txt") as F:
   data = []
   N, K, M = map(int, F.readline().split())
   for i in range(N):
     size, cost = map(int, F.readline().split())
     data.append( (size, cost) )

data.sort( reverse=True )

def valid( dPrev, dNext ):
  return dNext[0] <= dPrev[0]-K

MAXCOUNT = 200

# dp[count][i] <- minCost
dp = [ [float("inf")]*N for cost in range(MAXCOUNT) ]
dp[1] = [cost for size, cost in data]

for k in range(2,MAXCOUNT):

  for i, (size, cost) in enumerate(data):
    prevCost = [ dp[k-1][j] for j in range(N)
                            if valid(data[j], data[i]) and
                               dp[k-1][j] + cost <= M ]
    if prevCost:
      dp[k][i] = min(prevCost) + cost

  print( k, min(dp[k]) )

  if isinf( min(dp[k]) ):
    break




