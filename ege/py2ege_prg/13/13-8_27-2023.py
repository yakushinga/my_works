"""
На каждом километре дороги с двусторонним движением расположен пункт приёма
мусора. В одном из пунктов нужно построить мусороперерабатывающий завод.
Этот пункт нужно выбрать так, чтобы суммарная стоимость перевозки мусора
была минимальной. В первой строке файла input.txt записано натуральное число
N – количество пунктов приёма. В каждой из следующих N строк записано целое
неотрицательное число: количество килограммов мусора, которые нужно вывезти
с очередного пункта. Данные о пунктах записаны по порядку, начиная с пункта,
расположенного на нулевой отметке дороги. Стоимость перевозки равна
произведению расстояния от пункта до завода на количество килограммов
перевозимого мусора. Определите минимальную общую стоимость доставки мусора
со всех пунктов на мусороперерабатывающий завод.

(Ответ: 149515)
"""
with open("i/input_8.txt") as F:
  N = int( F.readline() )
  data = [ int(s) for s in F ]

p = [0]*(N+1)
for i in range(1, N+1):
  p[i] = p[i-1] + data[i-1]

cost = sum( data[i]*i for i in range(N) )
minCost = cost
for i in range(1, N):
  #cost += p[i] - (p[-1] - p[i])
  cost += 2*p[i] - p[-1]
  minCost = min( cost, minCost )

print( minCost )

print('------------------------------------------')
with open("i/input_8.txt") as F:
  N = int( F.readline() )
  data = [ int(s) for s in F ]

p, s = 0, sum(data)
cost = sum( data[i]*i for i in range(N) )
minCost = cost
for i in range(1, N):
  p += data[i-1]
  cost += 2*p - s
  minCost = min( cost, minCost )

print( minCost )

print('------------------------------------------')

with open("i/input_8.txt") as F:
  N = int( F.readline() )
  data = [ int(s) for s in F ]

minCost = float('inf')
for i in range(N):
  cost = sum( data[j]*abs(i-j) for j in range(N) )
  minCost = min( cost, minCost )

print( minCost )