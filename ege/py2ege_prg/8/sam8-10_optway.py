"""
Между населёнными пунктами A, B, C, D, E, F построены дороги, протяженность
которых (в километрах) приведена в таблице. Отсутствие числа в таблице означает,
что прямой дороги между пунктами нет. Определите длину кратчайшего пути между
пунктами A и F, не проходящего через пункт C.
Рис. 8.6.
"""
graph = { 'A': {'B': 7, 'C': 4, 'D': 8, 'F': 16},
          'B': {'A': 7, 'D': 3},
          'C': {'A': 4, 'D': 3},
          'D': {'A': 8, 'B': 3, 'C': 3, 'E': 5, 'F': 3},
          'E': {'D': 5, 'F': 5},
          'F': {'A': 16, 'D': 3, 'E': 5} }

INF = float('inf')
def optWay( way, end, curLen = 0 ):
  cur = way[-1]
  if cur == end:
    return curLen if 'C' not in way else INF
  minLen = INF
  for nxt in graph[cur]:
    if nxt not in way:
      minLen = min( optWay(way+nxt, end,
                    curLen+graph[cur][nxt]), minLen )
  return minLen

print( optWay('A', 'F') )

#-------------------------------------------

INF = float('inf')
def optWay( way, end, curLen = 0 ):
  if way[-1] == end:
    if 'C' not in way and curLen < INF:
      print( curLen, way )
      return curLen
    return INF
  return min ( (optWay( way+nxt, end,
                       curLen+graph[way[-1]][nxt] )
               for nxt in graph[way[-1]]
               if nxt not in way), default=INF )

print( optWay('A', 'F') )

#-------------------------------------------
print( 'Без ограничений на C:' )

INF = float('inf')
def optWay( way, end, curLen = 0 ):
  cur = way[-1]
  if cur == end:
    return curLen
  minLen = INF
  for nxt in graph[cur]:
    if nxt not in way:
      minLen = min( optWay(way+nxt, end,
                    curLen+graph[cur][nxt]), minLen )
  return minLen

print( optWay('A', 'F') )

#-------------------------------------------

INF = float('inf')
def optWay( way, end, curLen = 0 ):
  if way[-1] == end:
    if curLen < INF:
      print( curLen, way )
    return curLen
  return min ( (optWay( way+nxt, end,
                       curLen+graph[way[-1]][nxt])
                for nxt in graph[way[-1]]
                if nxt not in way), default=INF )

print( optWay('A', 'F') )
