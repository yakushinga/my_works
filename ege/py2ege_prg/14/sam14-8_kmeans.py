"""
В файле data14-8.txt записаны координаты точек, составляющие четыре
кластера сложной формы. Известно, что количество точек не превышает 10 000.
Определите координаты центра каждого кластера, затем вычислите два числа:
Px – среднее арифметическое абсцисс центров кластеров, и Py – среднее
арифметическое ординат центров кластеров. В ответе запишите два числа:
сначала целую часть произведения Px × 10 000, затем целую часть
произведения Py × 10 000.
Аномалии - группы не более чем из 10 точек, отстоящие более чем на 1 от любого
кластtра, - при вычислениях учитывать не нужно.

=== Четыре кластера сложной формы + аномалии ===

Метод: k-средних (k-медоидов). Неверное разбиение на кластеры.
Результат: 89758 6520 (неверный ответ).

Ответ: 92513 7039
"""

import math
def dist( p1, p2 ):
  return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2) ** 0.5
  return math.hypot( p1[0] - p2[0], p1[1] - p2[1] )

def getCenter( cluster ):
  minSumDist = float('inf')
  for p0 in cluster:
    sumDist = sum( math.dist(p0,p)
                   for p in cluster )
    if sumDist < minSumDist:
      minSumDist = sumDist
      center = p0
  return center

data = []
for s in open('data/data14-8.txt'):
  x, y = s.replace(',','.').split()
  data.append( (float(x), float(y)) )

from timeit import default_timer
t0 = default_timer()

K = 8 # количество кластеров данные + аномалии
centers = [(4.5, 4.8), (7, 0), (12, 2), (14, -3),
           (0, 8), (3, -3), (15.5, -6), (15, 6) # аномалии
           ]
oldCenters = []
while centers != oldCenters:
  oldCenters = centers
  clusters = [ [] for i in range(K) ]
  for p in data:
    distToCenters = [ dist(p,center) for center in centers ]
    k = distToCenters.index( min(distToCenters) )
    clusters[k].append( p )
  centers = [ getCenter(cluster) for cluster in clusters ]

clusters = [ cluster for cluster in clusters
                     if len(cluster) > 10 ]
K = len(clusters)
centers = [ getCenter(cluster) for cluster in clusters ]

print( "Центры:\n", centers )
print( f"Время: {default_timer()-t0:0.3f} с" )

Px = sum( centers[k][0] for k in range(K) ) / K
Py = sum( centers[k][1] for k in range(K) ) / K

print( int(Px*10000), int(Py*10000) )

from turtle import *
tracer(0)
up()
hideturtle()
colors = ['red', 'green', 'blue', 'magenta', 'black', 'orange', 'cyan', 'brown']
scale, shiftX, shiftY = 20, 200, 50
for i, cluster in enumerate(clusters):
  for x, y in cluster:
    goto( x*scale-shiftX, y*scale-shiftY )
    dot( 3, colors[i] )
done()
