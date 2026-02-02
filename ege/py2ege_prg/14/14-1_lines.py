"""
(Демо-2025)
В файле input_1.txt записаны координаты точек, составляющие три кластера. Известно,
что количество точек не превышает 10 000.
Определите координаты центра каждого кластера, затем вычислите два числа:
Px – среднее арифметическое абсцисс центров кластеров, и Py – среднее
арифметическое ординат центров кластеров. В ответе запишите два числа:
сначала целую часть произведения Px × 10 000, затем целую часть
произведения Py × 10 000.

=== Три кластера, простой случай ===

Метод: ручное выделение кластеров с помощью условий.

Ответ: 37669 49991
"""
def clusterNo( x, y ):
  return 0 if x > 5 else \
         1 if y > 6 else \
         2

K = 3 # количество кластеров
clusters = [ [] for i in range(K) ]

for s in open('i/input_1.txt'):
  x, y = s.replace(',','.').split()
  x, y = float(x), float(y)
  k = clusterNo( x, y )
  clusters[k].append( (x, y) )

import math
def dist( p1, p2 ):
  return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2) ** 0.5
  return math.hypot( p1[0] - p2[0], p1[1] - p2[1] )

def getCenter0( cluster ):
  minSumDist = float('inf')
  for p0 in cluster:
    sumDist = sum( math.dist(p0,p)
                   for p in cluster )
    if sumDist < minSumDist:
      minSumDist = sumDist
      center = p0
  return center

def getCenter( cluster ):
  N = len(cluster)
  pMid = ( sum( p[0] for p in cluster ) / N,
           sum( p[1] for p in cluster ) / N )
  delta = 0.2
  pointsNearCenter = [p for p in cluster
                        if math.dist(pMid,p) < delta ]
  minSumDist = float('inf')
  for p0 in pointsNearCenter:
    sumDist = sum( math.dist(p0,p)
                   for p in cluster )
    if sumDist < minSumDist:
      minSumDist = sumDist
      center = p0
  return center

print( "Кластеры:" )
for cluster in clusters:
  print( len(cluster) )

from timeit import default_timer
t0 = default_timer()
centers = [ getCenter(cluster) for cluster in clusters ]

##centers = []
##for k in range(K):
##  minSumDist = float('inf')
##  for p0 in clusters[k]:
##    sumDist = sum( math.dist(p0,p)
##                   for p in clusters[k] )
##    if sumDist < minSumDist:
##      minSumDist = sumDist
##      center = p0
##  centers.append( center )

print( "Центры:\n", centers )
print( f"Время: {default_timer()-t0:0.3f} с" )

sumX, sumY = 0, 0
for k in range(K):
  sumX += centers[k][0]
  sumY += centers[k][1]
Px = sumX / K
Py = sumY / K

print( int(Px*10000), int(Py*10000) )

Px = sum( centers[k][0] for k in range(K) ) / K
Py = sum( centers[k][1] for k in range(K) ) / K

print( int(Px*10000), int(Py*10000) )

from turtle import *
tracer(0)
up()
hideturtle()
colors = ['red', 'green', 'blue', 'magenta', 'brown', 'cyan']
scale, shiftX, shiftY = 50, 150, 200
for i, cluster in enumerate(clusters):
  for x, y in cluster:
    goto( x*scale-shiftX, y*scale-shiftY )
    dot( 3, colors[i] )
done()
