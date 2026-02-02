"""
Вдоль автомагистрали расположены N населённых пунктов. Компания планирует
построить кафе в одном из посёлков. Согласно опросам, жители охотно посещают
кафе, если до него нужно добираться не более M км. Необходимо разместить кафе
так, чтобы его могли посещать как можно больше жителей соседних посёлков.
В первой строке файла input.txt записаны натуральные числа N – количество
населённых пунктов, и M – максимальное растояние от кафе до населённого пункта.
В каждой из следующих N строк записаны два целых неотрицательных числа:
расстояние от очередного населённого пункта до нуле-вой отметки автомагистрали
и количество жителей, которые живут в этом населённом пункте. Определите
максимальное количество жителей, которые смогут посещать кафе при его
оптимальном расположении.

(Ответ: 3274)
"""
with open('i/input_13.txt') as F:
  N, M = map( int, F.readline().split() )
  position = []
  data = []
  for _ in range(N):
    pos, count = map(int, F.readline().split())
    position.append( pos )
    data.append( count )

maxSum = 0
for i in range(N):
  s = 0
  for j in range(N):
    if abs(position[i]-position[j]) <= M:
      s += data[j]
  maxSum = max( s, maxSum )

print( maxSum )

print('----------------------------------------------')

L = R = 0
s = 0
while R < N and \
  position[R] - position[0] <= M:
  s += data[R]
  R += 1
maxSum = s
for i in range(1,N):
  while position[i]-position[L] > M:
    s -= data[L]
    L += 1
  while R < N and position[R]-position[i] <= M:
    s += data[R]
    R += 1
  maxSum = max( s, maxSum )

print( maxSum )
