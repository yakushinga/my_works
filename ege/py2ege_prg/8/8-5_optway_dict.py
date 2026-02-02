"""
Между населёнными пунктами A, B, C, D, E построены дороги, протяженность
которых (в километрах) приведена в таблице. Отсутствие числа в таблице означает,
что прямой дороги между пунктами нет. Определите длину кратчайшего пути между
пунктами A и B, проходящего через пункт C.
Рис. 8.6.
"""
graph = { 'A': {'C': 3, 'D': 1},
          'B': {'C': 4, 'D': 5, 'E': 1},
          'C': {'A': 3, 'B': 4, 'E': 2},
          'D': {'A': 1, 'B': 5, 'E': 1},
          'E': {'B': 1, 'C': 2, 'D': 1} }

INF = float('inf')
def optWay( way, end, curLen = 0 ):
  cur = way[-1]
  if cur == end:
    return curLen if 'C' in way else INF
  minLen = INF
  for nxt in graph[cur]:
    if nxt not in way:
      minLen = min( optWay(way+nxt, end,
                    curLen+graph[cur][nxt]), minLen )
  return minLen

print( optWay('A', 'B') )

#-------------------------------------------

INF = float('inf')
def optWay( way, end, curLen = 0 ):
  if way[-1] == end:
    return curLen if 'C' in way else INF
  return min ( optWay( way+nxt, end,
                       curLen+graph[way[-1]][nxt])
               for nxt in graph[way[-1]]
               if nxt not in way )

print( optWay('A', 'B') )

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

print( optWay('A', 'B') )

#-------------------------------------------

INF = float('inf')
def optWay( way, end, curLen = 0 ):
  if way[-1] == end:
    return curLen
  return min ( optWay( way+nxt, end,
                       curLen+graph[way[-1]][nxt])
               for nxt in graph[way[-1]]
               if nxt not in way )

print( optWay('A', 'B') )
