"""
У медицинской компании есть N пунктов приёма биоматериалов на анализ. В первой
строке файла input.txt записано натуральное число N – количество пунктов приёма.
В каждой из следующих N строк записаны два целых неотрицательных числа:
расстояние от очередного пункта до нуле-вой отметки автомагистрали и количество
пробирок, которые нужно перевезти из этого пункта в лабораторию. Пробирки
перевозят в специальных контейнерах вместимостью не более 36 штук. Стоимость
перевозки равна произведению расстояния от пункта до лаборатории на количество
перевозимых контейнеров. Общая стоимость перевозки за день равна сумме
стоимостей перевозок из каждого пункта в лабораторию. Лабораторию расположили
в одном из пунктов приёма биоматериалов таким образом, что общая стоимость
доставки биоматериалов из всех пунктов минимальна. Определите минимальную общую
стоимость доставки.

Ответ: 51063
"""
with open("i/input_9.txt") as F:
  N = int( F.readline() )
  K = 36
  position = []
  data = []
  for s in F:
    pos, x = map( int, s.split() )
    position.append( pos )
    data.append( x//K if x % K == 0 else x//K + 1 )

p = 0
s = sum(data)
cost = sum( data[i]*(position[i]-position[0])
            for i in range(N) )
minCost = cost
for i in range(1, N):
  p += data[i-1]
  delta = position[i] - position[i-1]
  cost += (2*p - s)*delta
  minCost = min( cost, minCost )

print( minCost )

print('------------------------------------')

with open("i/input_9.txt") as F:
  N = int( F.readline() )
  K = 36
  position = []
  data = []
  for s in F:
    pos, x = map( int, s.split() )
    position.append( pos )
    data.append( x//K if x % K == 0 else x//K + 1 )

p = [0]*(N+1)
for i in range(1, N+1):
  p[i] = p[i-1] + data[i-1]

cost = sum( data[i]*(position[i]-position[0])
            for i in range(N) )
minCost = cost
for i in range(1, N):
  delta = position[i] - position[i-1]
  cost += (2*p[i] - p[-1])*delta
  minCost = min( cost, minCost )

print( minCost )

print('------------------------------------')

with open("i/input_9.txt") as F:
  N = int( F.readline() )
  K = 36
  position = []
  data = []
  for s in F:
    pos, x = map( int, s.split() )
    position.append( pos )
    data.append( x//K if x % K == 0 else x//K + 1 )

minCost = float('inf')
for i in range(N):
  cost = 0
  for j in range(N):
    cost += data[j] * abs( position[i] - position[j] )
  minCost = min( cost, minCost )

print( minCost )