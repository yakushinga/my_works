"""
В файле data14-5.txt записаны координаты точек, составляющие три
кластера формы. Известно, что количество точек не превышает 10 000.
Определите координаты центра каждого кластера, затем вычислите два числа:
Px – среднее арифметическое абсцисс центров кластеров, и Py – среднее
арифметическое ординат центров кластеров. В ответе запишите два числа:
сначала целую часть произведения Px × 10 000, затем целую часть
произведения Py × 10 000.
Аномалии - группы не более чем из 10 точек, отстоящие более чем на 1 от любого
кластtра, - при вычислениях учитывать не нужно.

=== Три кластера + аномалии ===

Метод: DBSCAN. Разбиение на кластеры с мнимыми аномалиями, которые не влияют на результат.

Ответ: 41107 48687
"""

data = []
for s in open('data/data14-5.txt'):
  x, y = s.replace(',','.').split()
  data.append( (float(x), float(y)) )

import math
def dist( p1, p2 ):
  return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2) ** 0.5
  return math.hypot( p1[0] - p2[0], p1[1] - p2[1] )

eps = 0.5

# Нерекурсивная версия
def getCluster( p0, eps ):
  data.remove( p0 )
  cluster = [ p0 ]
  for p in cluster:
    neighbors = [ n for n in data
                    if math.dist(n, p) < eps ]
    cluster += neighbors
    for n in neighbors:
      data.remove( n )
  return cluster

def getCenter( cluster ):
  minSumDist = float('inf')
  for p0 in cluster:
    sumDist = sum( math.dist(p0,p)
                   for p in cluster )
    if sumDist < minSumDist:
      minSumDist = sumDist
      center = p0
  return center

from timeit import default_timer
t0 = default_timer()
print( "Кластеры:" )
clusters = []
while data:
  cluster = getCluster( data[0], eps )
  clusters.append( cluster )
  print( len(cluster) )
print( f"Разбиение на кластеры: {default_timer()-t0:0.3f} с" )

clusters = [ cluster for cluster in clusters
                     if len(cluster) > 10 ]

K = len(clusters)

t0 = default_timer()
centers = [ getCenter(cluster) for cluster in clusters ]
print( "Центры:\n", centers )
print( f"Поиск центров: {default_timer()-t0:0.3f} с" )

Px = sum( centers[k][0] for k in range(K) ) / K
Py = sum( centers[k][1] for k in range(K) ) / K

print( int(Px*10000), int(Py*10000) )

from turtle import *
tracer(0)
up()
hideturtle()
colors = ['red', 'green', 'blue', 'orange', 'cyan', 'magenta']
scale, shiftX, shiftY = 50, 150, 200
for i, cluster in enumerate(clusters):
  for x, y in cluster:
    goto( x*scale-shiftX, y*scale-shiftY )
    dot( 3, colors[i] )
done()
