"""
(Демо-2023) На рисунке представлена схема дорог, связывающих города
А, Б, В, Г, Д, Е, Ж, И, К, Л. По каждой дороге можно двигаться только в
одном направлении, указанном стрелкой. Определите количество различных
путей ненулевой длины, которые начинаются и заканчиваются в городе Е,
не содержат этот город в качестве промежуточного пункта и проходят через
промежуточные города не более одного раза.
"""
graph = { 'А': "БГ", 'Б': "ВД", 'В': "АГД", 'Г': "ЕЖ",
          'Д': "ЕИЛ", 'Е': "ВЛ", 'Ж': "Е",
          'И': "Л", 'К': "Ж", 'Л': "ЖК" }

count = 0
def searchLoops( way ):
  cur = way[-1]
  if len(way) > 1 and cur == way[0]:
    #print( way )
    global count
    count += 1
    return
  for nxt in graph[cur]:
    if nxt not in way or nxt == way[0]:
      searchLoops( way + nxt )

searchLoops( 'Е' )
print( count )

#-------------------------------------------

s = "АБГ БВД ВАГД ГЕЖ ДЕИЛ ЕВЛ ЖЕ ИЛ КЖ ЛЖК"
graph = { x[0]: x[1:] for x in s.split() }

def searchLoops( way ):
  cur = way[-1]
  if len(way) > 1 and cur == way[0]:
    #print( way )
    return 1
  count = 0
  for nxt in graph[cur]:
    if nxt not in way or nxt == way[0]:
      count += searchLoops( way + nxt )
  return count

print( searchLoops('Е') )

#-------------------------------------------

s = "АБГ БВД ВАГД ГЕЖ ДЕИЛ ЕВЛ ЖЕ ИЛ КЖ ЛЖК"
graph = { x[0]: x[1:] for x in s.split() }

def searchLoops( way ):
  if len(way) > 1 and way[-1] == way[0]:
    return 1
  return sum( searchLoops(way + nxt)
              for nxt in graph[way[-1]]
              if nxt not in way or nxt == way[0] )

print( searchLoops('Е') )








