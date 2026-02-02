"""
Аполлон составляет все возможные семибуквенные слова перестановкой букв своего
имени. Сколько Аполлон может составить различных слов, в которых нет
одинаковых букв, стоящих рядом?
"""
from itertools import permutations

count = 0
for w in set(permutations('АПОЛЛОН')):
  s = ''.join( w )
  if 'ОО' not in s and 'ЛЛ' not in s:
    count += 1

print( count )

count = len( [ s for w in set(permutations('АПОЛЛОН'))
                if 'ОО' not in (s:=''.join(w)) and 'ЛЛ' not in s ] )
print( count )

from itertools import permutations
print( len( [ s
              for w in set(permutations('АПОЛЛОН'))
              if 'ОО' not in (s:=''.join(w)) and
                 'ЛЛ' not in s ] ) )

print( sum( 1 for w in set(permutations('АПОЛЛОН'))
             if 'ОО' not in (s:=''.join(w)) and 'ЛЛ' not in s ) )

print( sum( 'ОО' not in (s:=''.join(w)) and 'ЛЛ' not in s
            for w in set(permutations('АПОЛЛОН'))) )
