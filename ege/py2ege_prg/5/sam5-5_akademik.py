"""
Вася переставляет буквы в слове АКАДЕМИК, составляя новые слова, в которых
никакие две гласные и никакие две согласные буквы не стоят рядом.
Сколько различных слов может составить Вася?
(Ответ: 1152)
"""
from itertools import permutations

count = 0
for w in set(permutations('АКАДЕМИК')):
  s = ''.join( w )
  s = s.replace( 'Е', 'А' )
  s = s.replace( 'И', 'А' )
  s = s.replace( 'Д', 'К' )
  s = s.replace( 'М', 'К' )
  if 'АА' not in s or 'КК' not in s:
    count += 1

print( count )

#-----------------------------------

count = 0
for w in set(permutations('АКАДЕМИК')):
  s = ''.join( w ).replace( 'Е', 'А' ).replace( 'И', 'А' ) \
        .replace( 'Д', 'К' ).replace( 'М', 'К' )
  if 'АА' not in s or 'КК' not in s:
    count += 1

print( count )


#-----------------------------------

count = 0
for w in set(permutations('АКАДЕМИК')):
  s = ''.join( w )
  for c in 'АИЕ': s = s.replace(c, 'g')
  for c in 'КДМ': s = s.replace(c, 's')
  if 'gg' not in s or 'ss' not in s:
    count += 1

print( count )

#-----------------------------------