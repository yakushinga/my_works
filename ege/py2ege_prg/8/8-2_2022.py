"""
(Демо-2022) На рисунке представлена схема дорог, связывающих города
А, Б, В, Г, Д, Е, Ж, З, И, К, Л, М. По каждой дороге можно двигаться
только в одном направлении, указанном стрелкой. Сколько существует
различных путей из города А в город М, проходящих через город В?
"""
graph = { 'А': "БВГД", 'Б': "ВЕ", 'В': "ЖЗ", 'Г': "ВЗ",
          'Д': "ГЗ", 'Е': "ЖИ", 'Ж': "И", 'З': "ЖИ",
          'И': "КЛ", 'К': "М", 'Л': "М" }

count = 0
def search( way, end ):
  cur = way[-1]
  if cur == end:
    if 'В' in way:
      global count
      count += 1
    return
  for nxt in graph[cur]:
    search( way + nxt, end )

search( 'А', 'М' )
print( count )

#-----------------------------------

s = "АБВГД БВЕ ВЖЗ ГВЗ ДГЗ ЕЖИ ЖИ ЗЖИ ИКЛ КМ ЛМ"
graph = { x[0]: x[1:] for x in s.split() }

def search( way, end ):
  cur = way[-1]
  if cur == end:
    #return 1 if 'В' in way else 0
    return 'В' in way
  count = 0
  for nxt in graph[cur]:
    count += search( way + nxt, end )
  return count

print( search('А', 'М') )

#-----------------------------------

s = "АБВГД БВЕ ВЖЗ ГВЗ ДГЗ ЕЖИ ЖИ ЗЖИ ИКЛ КМ ЛМ"
graph = { x[0]: x[1:] for x in s.split() }

def search( way, end ):
  if way[-1] == end:
    return 'В' in way
  return sum( search( way + nxt, end )
              for nxt in graph[way[-1]] )

print( search('А', 'М') )





