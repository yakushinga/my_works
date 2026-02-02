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

# Автор: М. Ишимов

tbl = "234567 17 157 156 134 14 123".split()
graph = "AC AG BC BD CD CE CF CG DE EF FG".split()

from itertools import permutations

print( "1 2 3 4 5 6 7" )
for	p in permutations("ABCDEFG"):
  for x, y in graph:
    i, j = p.index(x), p.index(y)
    if str(j+1) not in tbl[i]:
      break
  else:
    print( *p )

print( '------------------' )
print( "1 2 3 4 5 6 7" )
for	p in permutations("ABCDEFG"):
  if all( str(p.index(y)+1) in tbl[p.index(x)]
          for x, y in graph ):
    print( *p )
