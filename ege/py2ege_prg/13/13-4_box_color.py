"""
(А. Кабанов) В магазине для упаковки подарков есть N кубических коробок красного,
зелёного и синего цветов. Самой интересной считается упаковка подарка по принципу
матрёшки: подарок упаковывается в одну из коробок, та в свою очередь в другую
коробку и т. д. Одну коробку можно поместить в другую, ес-ли длина её стороны
хотя бы на K единиц меньше длины сто-роны другой коробки. Кроме того, цвета
соседних коробок должны различаться.
Определите наибольшее количество коробок, которое можно использовать для упаковки
одного подарка, и максимально возможную длину стороны самой маленькой коробки,
где будет находиться подарок. Размер подарка позволяет поместить его в самую
маленькую коробку.
В первой строке файла input.txt записаны натуральные числа N – количество
коробок в магазине, и K – минимально допустимая разница длин сторон соседних
коробок в матрёшке. В каждой из следующих N строк записана длина стороны
очередной коробки и через пробел – цвет коробки (буква R, G или B).

Ответ: 628 4
"""
with open("i/input_4.txt") as F:
  N, K = map( int, F.readline().split() )
  data = []
  for _ in range(N):
    size, color = F.readline().split()
    data.append( (int(size), color) )

data.sort( reverse=True )

dp = [0]*N

def valid( dPrev, dNext ):
  return dNext[0] <= dPrev[0]-K and dNext[1] != dPrev[1]

for i in range(N):
  maxPrev = 0
  for j in range(i):
    if valid( data[j], data[i] ):
      maxPrev = max( dp[j], maxPrev )
  dp[i] = maxPrev + 1

for i in range(N):
  maxPrev = max( (dp[j] for j in range(i)
                  if valid(data[j], data[i])), default=0 )
  dp[i] = maxPrev + 1

"""
for i, (size, color) in enumerate(data):
  prevBoxes = [ dp[j] for j in range(i)
            if data[i][0] <= data[j][0]-K and data[j][1] != data[i][1] ]
  dp[i] = max( prevBoxes, default=0 ) + 1
"""

M = max(dp)
print( M, max( data[i][0]
               for i in range(N) if dp[i] == M ) )
print( M, data[dp.index(M)][0] )

m = dp.index(M)
stack = [data[m]]
while dp[m] > 1:
  prev = [ i for i in range(m)
             if valid(data[i], data[m]) and dp[i] == dp[m]-1 ]
  m = prev[0]
  stack.append( data[m] )
# print( stack )


