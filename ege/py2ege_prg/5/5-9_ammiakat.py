"""
Петя переставляет буквы в слове АММИАКАТ, составляя слова, в которых обязательно
две гласные или две согласные буквы стоят рядом. Сколько различных слов
может составить Петя?
"""
from itertools import permutations

count = 0
for w in set(permutations('АММИАКАТ')):
  s = ''.join( w )
  s = s.replace( 'И', 'А' )
  s = s.replace( 'К', 'М' )
  s = s.replace( 'Т', 'М' )
  if 'АА' in s or 'ММ' in s:
    count += 1

print( count )

#-----------------------------------

count = 0
for w in set(permutations('АММИАКАТ')):
  s = ''.join( w ).replace( 'И', 'А' ) \
        .replace( 'К', 'М' ).replace( 'Т', 'М' )
  if 'АА' in s or 'ММ' in s:
    count += 1

print( count )


#-----------------------------------

count = 0
for w in set(permutations('АММИАКАТ')):
  s = ''.join( w )
  for c in 'АИ': s = s.replace(c, 'g')
  for c in 'МКТ': s = s.replace(c, 's')
  if 'gg' in s or 'ss' in s:
    count += 1

print( count )

