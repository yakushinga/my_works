"""
В файле data14-4.txt записаны координаты точек, составляющие четыре
кластера сложной формы. Известно, что количество точек не превышает 10 000.
Определите координаты центра каждого кластера, затем вычислите два числа:
Px – среднее арифметическое абсцисс центров кластеров, и Py – среднее
арифметическое ординат центров кластеров. В ответе запишите два числа:
сначала целую часть произведения Px × 10 000, затем целую часть
произведения Py × 10 000.

=== Четыре кластера сложной формы ===

Метод: DBSCAN.

Ответ: 6994 7431
"""

data = []
for s in open('data/data14-4.txt'):
  x, y = s.replace(',','.').split()
  data.append( (float(x), float(y)) )

import math
def dist( p1, p2 ):
  return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2) ** 0.5
  return math.hypot( p1[0] - p2[0], p1[1] - p2[1] )

eps = 0.4

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
scale, shiftX, shiftY = 25, 50, 50
for i, cluster in enumerate(clusters):
  for x, y in cluster:
    goto( x*scale-shiftX, y*scale-shiftY )
    dot( 3, colors[i] )
done()
