"""
В файле data13-7.txt записаны показания прибора, который каждую минуту
регистрирует напряжение в сети. Определите четыре таких переданных числа, чтобы
между моментами передачи любых двух из них прошло не менее K мин., а сумма
этих четырёх чисел была минимально возможной. Запишите в ответе найденную сумму.
В первой строке файла записаны натуральные числа N и K, разделённые пробелом.
В каждой из следующих N строк записано одно целое число – показание прибора в
соответствующую минуту.

Ответ: –161800
"""
with open("data/data13-9.txt") as F:
  N, K = map( int, F.readline().split() )
  data = [ int(s) for s in F ]

INF = float('inf')
s1Min = s2Min = s3Min = s4Min = INF
for i in range(3*K,N):
  s1Min = min( data[i-3*K], s1Min )
  s2Min = min( data[i-2*K] + s1Min, s2Min )
  s3Min = min( data[i-K] + s2Min, s3Min )
  s4Min = min( data[i] + s3Min, s4Min )
print( s4Min )

print('-----------------------------')

"""
s4Min = float('inf')
for i in range(N):
 for j in range(i+K,N):
  for k in range(j+K,N):
   for m in range(k+K,N):
     s = data[i] + data[j] + data[k] + data[m]
     s4Min = min( s, s4Min )

print( s4Min )
"""

