"""
Между населёнными пунктами A, B, C, D, E построены дороги, протяженность
которых (в километрах) приведена в таблице. Отсутствие числа в таблице означает,
что прямой дороги между пунктами нет. Определите длину кратчайшего пути между
пунктами A и B, проходящего через пункт C.
Рис. 8.6.
"""
INF = float('inf')
W = [ [INF, INF, 3, 1, INF],
      [INF, INF, 4, 5, 1],
      [3, 4, INF, INF, 2],
      [1, 5, INF, INF, 1],
      [INF, 1, 2, 1, INF] ]
N = len(W)

def optWay( way, end, curLen = 0 ):
  cur = way[-1]
  if cur == end:
    return curLen if 2 in way else INF
  minLen = INF
  for nxt in range(N):
    if nxt not in way:
      minLen = min( minLen,
         optWay( way+[nxt], end, curLen+W[cur][nxt]) )
  return minLen

print( optWay([0], 1) )

print('-------------------------------------------')

INF = float('inf')
def optWay( way, end, curLen = 0 ):
  if way[-1] == end:
    return curLen if 2 in way else INF
  return min ( optWay( way+[nxt], end,
                       curLen+W[way[-1]][nxt])
               for nxt in range(N)
               if nxt not in way )

print( optWay([0], 1) )

print('-------------------------------------------')

INF = float('inf')
def optWay( way, end, curLen = 0 ):
  if way[-1] == end:
    if 2 in way and curLen < INF:
      print( curLen, ''.join( "ABCDE"[v] for v in way ) )
      return curLen
    return INF
  return min ( (optWay( way+[nxt], end,
                       curLen+W[way[-1]][nxt])
                for nxt in range(N)
                if nxt not in way), default=INF )

print( optWay([0], 1) )

print('-------------------------------------------')

print( 'Без ограничений на C:' )

INF = float('inf')
def optWay( way, end, curLen = 0 ):
  cur = way[-1]
  if cur == end:
    return curLen
  minLen = INF
  for nxt in range(N):
    if nxt not in way:
      minLen = min( optWay(way+[nxt], end,
                    curLen+W[cur][nxt]), minLen )
  return minLen

print( optWay([0], 1) )

#-------------------------------------------

INF = float('inf')
def optWay( way, end, curLen = 0 ):
  if way[-1] == end:
    return curLen
  return min ( (optWay( way+[nxt], end,
                       curLen+W[way[-1]][nxt])
                for nxt in range(N)
                if nxt not in way), default=INF )

print( optWay([0], 1) )
