"""
В файле data14-3_bananas.txt записаны координаты точек, составляющие три
кластера сложной формы. Известно, что количество точек не превышает 10 000.
Определите координаты центра каждого кластера, затем вычислите два числа:
Px – среднее арифметическое абсцисс центров кластеров, и Py – среднее
арифметическое ординат центров кластеров. В ответе запишите два числа:
сначала целую часть произведения Px × 10 000, затем целую часть
произведения Py × 10 000.

=== Три кластера сложной формы ===

Метод: k-средних (k-медоидов).

Неверное разбиение на кластеры.
Результат: 34381 47875 (неверный ответ)

Ответ: 34461 47809
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
for s in open('data/data14-3_bananas.txt'):
  x, y = s.replace(',','.').split()
  data.append( (float(x), float(y)) )

from timeit import default_timer
t0 = default_timer()

K = 3 # количество кластеров
centers = [(0.3, 5), (5, 3.5), (4.3, 7)]
oldCenters = []
while centers != oldCenters:
  oldCenters = centers
  clusters = [ [] for i in range(K) ]
  for p in data:
    distToCenters = [ dist(p,center) for center in centers ]
    k = distToCenters.index( min(distToCenters) )
    clusters[k].append( p )
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
colors = ['red', 'green', 'blue', 'magenta']
scale, shiftX, shiftY = 50, 200, 250
for i, cluster in enumerate(clusters):
  for x, y in cluster:
    goto( x*scale-shiftX, y*scale-shiftY )
    dot( 3, colors[i] )
done()
