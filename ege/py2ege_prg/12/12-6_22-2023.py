"""
(Демо-2023) В файле input.csv содержится информация о совокупности вычислительных
процессов, которые могут выполняться параллельно или последовательно. Будем
говорить, что про-цесс B зависит от процесса A, если для выполнения процесса
B необходимы результаты выполнения процесса A. В этом случае процессы могут
выполняться только последовательно. Информация о процессах представлена в файле
в виде таблицы. В первом столбце таблицы указан идентификатор процесса (ID), во
втором столбце таблицы – время его выполнения в миллисекундах, в третьем столбце
перечислены с разделителем «;» ID процессов, от которых зависит данный процесс.
Если процесс является независимым, то в третьем столбце таблицы указано значение 0.
Определите минимальное время, через которое завершится выполнение всей
совокупности процессов при условии, что все независимые друг от друга процессы
могут выполняться параллельно.
Типовой пример организации данных в файле:
1;4;0
2;3;0
3;1;"1; 2"
4;7;3
В данном случае независимые процессы 1 и 2 могут выполняться параллельно, при
этом процесс 1 завершится через 4 мс, а процесс 2 – через 3 мс с момента старта.
Процесс 3 может начаться только после завершения обоих процессов 1 и 2, то есть,
через 4 мс после старта. Он длится 1 мс и закон-чится через 4 + 1 = 5 мс после
старта. Выполнение процесса 4 может начаться только после завершения процесса 3,
то есть, через 5 мс. Он длится 7 мс, так что минимальное вре-мя завершения всех
процессов равно 5 + 7 = 12 мс.
(Ответ: 17)
"""
with open("i/input_6.csv") as F:
  finalTime = {0: 0}
  for s in F:
    s = s.replace(';', ' ').replace('"','')
    pid, t, *dependsOn = map( int, s.split() )
    finalTime[pid] = t + max( finalTime[p] for p in dependsOn )

print( max(finalTime.values()) )

print('----------------------------------------------')

with open("i/input_6.csv") as F:
  data = {}
  for s in F:
    s = s.replace('"', '')\
         .replace(';', ' ')
    pid, t, *dependsOn  = map( int, s.split() )
    data[pid] = ( t, dependsOn )

finalTime = {0: 0}
for id in list(data.keys()):
  t, dependsOn = data[id]
  finalTime[id] = t + max( finalTime[x] for x in dependsOn )

print( max(finalTime.values()) )

print('----------------------------------------------')

with open("i/input_6.csv") as F:
  data = {}
  for s in F:
    s = s.replace(';', ' ').replace('"', '')
    pid, t, *dependsOn  = map( int, s.split() )
    data[pid] = ( t, dependsOn )

finalTime = {0: 0}
while data:
  for id in list(data.keys()):
    t, dependsOn = data[id]
    if all( (x in finalTime) for x in dependsOn ):
      finalTime[id] = t + max( finalTime[x] for x in dependsOn )
      del data[id]

print( finalTime )
print( max(finalTime.values()) )

print('----------------------------------------------')

with open("i/input_6.csv") as F:
  data = {}
  for s in F:
    s = s.strip().replace('"', '')\
                 .replace(';', ' ')
    pid, t, *dependsOn  = map( int, s.split() )
    data[pid] = ( t, dependsOn )

finalTime = {0: 0}
def findFinalTime( pid ):
  if pid not in finalTime:
    t, dependsOn = data[pid]
    finalTime[pid] = t + \
      max( findFinalTime(p) for p in dependsOn )
  return finalTime[pid]

print( max( findFinalTime(pid) for pid in data ) )
