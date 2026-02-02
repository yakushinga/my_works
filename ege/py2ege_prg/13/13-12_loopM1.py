"""
На каждом километре кольцевой дороги расположены N хуторов, в которые нужно
доставлять товары с помощью роботов-доставщиков. У компании хватает денег
только на один пункт доставки. Зарядка робота ограничена, её хватает на то,
чтобы проехать M км в одну сторону и вернуться в пункт доставки для подзарядки.
В первой строке файла input.txt записаны два натуральных числа: N – количество
хуторов и M – максимальное расстояние, которое может проехать робот в одну
сторону. В каждой из следующих N строк записано натуральное число – количество
товаров, которые нужно доставить на хутор. Данные о хуторах перечисляются по
порядку, начиная с нулевой отметки дороги. Определите, на каком хуторе нужно
построить пункт доставки, чтобы роботы смогли доставить наибольшее количество
товаров. В ответе запишите найденное количество товаров.

Ответ: 75 4174
"""

fName = 'i/input_12.txt'

with open( fName ) as F:
  N, M = map( int, F.readline().split() )
  data = [ int(s) for s in F ]

data = data*2
s = sum( data[:2*M+1] )
iMax, maxSum = 0, s
for i in range(1, N):
  s += data[i+2*M] - data[i-1]
  if s > maxSum:
    iMax, maxSum = i, s

print( iMax+M, maxSum )

print('------------------------------------------')

with open( fName ) as F:
  N, M = map( int, F.readline().split() )
  data = [ int(s) for s in F ]

s = sum( data[:2*M+1] )
iMax, maxSum = 0, s
for i in range(1, N):
  s += data[(i+2*M)%N] - data[i-1]
  if s > maxSum:
    iMax, maxSum = i, s

print( iMax+M, maxSum )

print('------------------------------------------')

with open( fName ) as F:
  N, M = map( int, F.readline().split() )
  data = [ int(s) for s in F ]

def dist( i, j ):
  d1 = abs(i - j)
  return min( d1, N-d1)

iMax, maxSum = 0, 0
for i in range(N):
  s = sum( data[j] for j in range(N)
                   if dist(i, j) <= M )
  if s > maxSum:
    iMax = i
    maxSum = s

print( iMax, maxSum )
