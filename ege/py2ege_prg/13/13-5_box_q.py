"""
В магазине для упаковки подарков есть N кубических коробок разной стоимости.
Самой интересной считается упаковка подарка по принципу матрёшки: подарок
упаковывается в одну из коробок, та в свою очередь в другую коробку и т. д. Одну
коробку можно поместить в другую, если длина её стороны хотя бы на K единиц меньше
длины стороны другой коробки.
Определите наименьшую стоимость упаковки, при которой количество вложенных друг в
друга коробок не меньше Q, и максимально возможную длину стороны самой маленькой
коробки, где будет находиться подарок. Размер подарка позволяет поместить его в
самую маленькую коробку.
В первой строке файла input.txt записаны натуральные числа N – количество коробок
в магазине, K – минимально допустимая разница длин сторон соседних коробок в матрёшке,
и Q – минимально допустимое количество вложенных коробок. В каждой из следующих N
строк записана длина стороны очередной коробки и через пробел – стоимость коробки.

Ответ: 650 14
"""
fName = "i/input_5.txt"
with open(fName) as F:
   data = []
   N, K, Q = map(int, F.readline().split())
   for i in range(N):
     size, cost = map(int, F.readline().split())
     data.append( (size, cost) )

data.sort( reverse=True )

dp = [ [0]*N for q in range(Q+1) ]

INF = float('inf')

def valid( dPrev, dNext ):
  return dNext[0] <= dPrev[0]-K

for i in range(N):
  dp[1][i] = data[i][1]

for q in range(2,Q+1):
  for i in range(N):
    prev = [ dp[q-1][j] for j in range(i)
                        if valid( data[j], data[i] ) ]
    dp[q][i] = min( prev, default=INF ) + data[i][1]

minCost = min( dp[Q] )
m = max( i for i in range(N)
           if dp[Q][i] == minCost )
print( minCost, data[m][0] )

q = Q
stack = [data[m]]
while q > 1:
  prev = [ i for i in range(m)
             if valid(data[i], data[m]) and
                dp[q-1][i] == dp[q][m]-data[m][1] ]
  m = prev[-1]
  q -= 1
  stack.append( data[m] )
# print( stack )


