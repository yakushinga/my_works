"""
Входной файл input.txt содержит сведения о заявках на проведение мероприятий
в конференц-зале. В первой строке входного файла находится натуральное число
N – количество заявок на проведение мероприятий. Следующие N строк содержат
пары чисел, обозначающих время начала и время окончания мероприятий (в минутах
от начала суток). Если время окончания одного мероприятия совпадает со
временем начала другого, то провести можно оба. Определите, какое максимальное
количество мероприятий можно провести в конференц-зале и каков при этом
максимально возможный перерыв между двумя последними мероприятиями.
"""
with open("i/input_5.txt") as F:
  N = int( F.readline() )
  data = []
  for s in F:
    t0, t1 = map( int, s.split() )
    data.append( (t0, t1) )

data.sort()

results = []
from functools import cache
@cache
def place( i, count = 0, tPrev = 0 ):
  count += 1
  results.append( (count, data[i][0]-tPrev) )
  tFree = data[i][1]
  for nxt in range( i+1, N ):
    if data[nxt][0] >= tFree:
      place( nxt, count, data[i][1] )

for iFirst in range(N):
  place( iFirst )

results.sort( reverse = True )
print( results[0] )

