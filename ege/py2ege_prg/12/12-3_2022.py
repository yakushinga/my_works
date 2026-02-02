"""
Системный администратор создаёт архив файлов на диске, объём которого меньше,
чем суммарный объём архивируемых файлов. В первой строке файла input.txt
записаны два натуральных числа: S – свободное место на диске и N – количеcтво
файлов. В каждой из следующих N строк записано одно натуральное число – размер файла.
Определите максимальное число файлов, которые можно сохранить в архиве, а также
максимальный размер файла, который может быть сохранён в архиве, при условии,
что количество сохранённых файлов максимально.
(Ответ: 568 50)
"""
with open("i/input_3.txt") as F:
  S, N = map( int, F.readline().split() )
  data = [ int(s) for s in F ]

data.sort()

"""
count = V = 0
while V+data[count] <= S:
  V += data[count]
  count += 1

print( count )

V -= data[count-1]

maxLast = 0
for i in range(count-1, N):
  if V + data[i] <= S :
    maxLast = data[i]

print( maxLast )
"""
print('----------------------------------------')

count = max( k for k in range(1,N+1)
               if sum(data[:k]) <= S )
print( count )

candidates = [ x for x in data[count-1:]
                 if sum(data[:count-1]) + x <= S ]

print( max(candidates) )
# или
print( candidates[-1] )

print('----------------------------------------')

print( count := max( k for k in range(1,N+1)
                       if sum(data[:k]) <= S ) )
print( max( x for x in data[count-1:]
              if sum(data[:count-1]) + x <= S) )
