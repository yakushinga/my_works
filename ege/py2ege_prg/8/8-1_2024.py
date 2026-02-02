"""
На рисунке изображена схема дорог N-ского района. В таблице звёздочкой
обозначено наличие дороги из одного населённого пункта в другой. Отсутствие
звёздочки означает, что такой дороги нет.
Рис. 8.2.
Каждому населённому пункту на схеме соответствует номер в таблице, но
неизвестно, какой именно номер. Определите, какие номера в таблице могут
соответствовать населённым пунктам E и F на схеме. В ответе запишите эти
два номера в возрастающем порядке без пробелов и знаков препинания.
"""
tbl = { 1: "234567",
        2: "17", 3: "157", 4: "156",
        5: "134", 6: "14", 7: "123"  }
g = { 'A': "CG", 'B': "CD", 'C': "ABDEFG", 'D': "BCE",
      'E': "CDF", 'F': "CEG", 'G': "ACF" }

from itertools import permutations

def subst( p ):
  g = {}
  for i, v in enumerate(p, start=1):
    s = tbl[i]
    for j, c in enumerate(p, start=1):
      s = s.replace( str(j), c )
    g[v] = ''.join(sorted(s))
  return g

print( "1 2 3 4 5 6 7" )
for p in permutations( "ABCDEFG" ):
  if g == subst( p ):
    print( *p )

#-----------------------------------------
print( '----------------------------------' )

tbl = { '1': "234567",
        '2': "17", '3': "157", '4': "156",
        '5': "134", '6': "14", '7': "123"  }
graph = { 'A': "CG", 'B': "CD", 'C': "ABDEFG", 'D': "BCE",
          'E': "CDF", 'F': "CEG", 'G': "ACF" }

from itertools import permutations

def subst( p ):
  s = str(tbl)
  for i, v in enumerate(p, start=1):
    s = s.replace( str(i), v )
  return eval(s)

def subst( p ):
  s = str(tbl)
  for i in range(1, len(p)+1):
    s = s.replace( str(i), p[i-1] )
  return eval(s)

vertices = graph.keys()
print( "1 2 3 4 5 6 7" )
for p in permutations( vertices ):
  g = subst( p )
  #if all( set(graph[v]) == set(g[v]) for v in vertices ):
  if all( sorted(g[v]) == sorted(graph[v]) for v in vertices ):
    print( *p )
    #print( "  ", g )



