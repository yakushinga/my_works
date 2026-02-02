"""
На рисунке схема дорог N-ского района изображена в виде графа, в таблице
содержатся сведения о длинах этих дорог (в километрах). Так как таблицу
и схему рисовали независимо друг от друга, то нумерация населённых пунктов
в таблице никак не связана с буквенными обозначениями на графе.
Определите длину пути BCDGA.
Рис. 8.8.
 (Ответ: 61)
"""
tbl = { '1': '257',
        '2': '1348', '3': '2568', '4': '27',
        '5': '136', '6': '35', '7': '14', '8': '23'  }
graph = { 'A': 'FG', 'B': 'CF', 'C': 'BDF', 'D': 'CEG',
          'E': 'DH', 'F': 'ABCG', 'G': 'ADFH', 'H': 'EG' }

from itertools import permutations

def subst( p ):
  s = str(tbl)
  for i in range(1, len(p)+1):
    s = s.replace( str(i), p[i-1] )
  return eval(s)

vertices = graph.keys()
print( '1 2 3 4 5 6 7 8' )
for p in permutations( vertices ):
  g = subst( p )
  if all( set(graph[v]) == set(g[v]) for v in vertices ):
    print( *p )

print( 14 + 16 + 10 + 21 )