"""
(Демо-2024) В файле input.txt записаны показания прибора, который каждую минуту регистрирует
напряжениев сети. Определите три таких переданных числа, чтобы между моментами
передачи любых двух из них прошло не менее K мин., а сумма этих трёх чисел была
максимально возможной. Запишите в ответе найденную сумму.
В первой строке файла записаны натуральные числа N и K, разделённые пробелом.
В каждой из следующих N строк за-писано одно целое число – показание прибора
в соответствующую минуту.

Ответ: 189536
"""
with open("i/input_7.txt") as F:
  N, K = map( int, F.readline().split() )
  data = [ int(s) for s in F ]

INF = float('inf')
s1Max = [data[0]]*N
s2Max = [-INF]*N
s3Max = [-INF]*N
for i in range(1,N):
  s1Max[i] = max( data[i], s1Max[i-1] )
for j in range( K ,N):
  s2Max[j] = max( data[j] + s1Max[ j-K],
                  s2Max[j-1] )
for m in range( 2*K,N):
  s3Max[m] = max( data[m] + s2Max[ m-K],
                  s3Max[m-1] )
print( s3Max[-1] )

INF = float('inf')
s1Max = s2Max = s3Max = -INF
for i in range(2*K,N):
  s1Max = max( data[i-2*K], s1Max )
  s2Max = max( data[i-K] + s1Max, s2Max )
  s3Max = max( data[i] + s2Max, s3Max )
print( s3Max )
