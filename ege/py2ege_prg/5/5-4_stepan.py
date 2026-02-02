"""
Степан составляет все возможные шестибуквенные слова из букв С, Т, Е, П, А, Н.
Каждая буква может входить в слово любое количество раз или не встречаться
совсем. Сколько Степан может составить различных слов, в которых ровно две
буквы Е?
"""
from itertools import product

k = 0
for w in product( 'СТЕПАН', repeat=6 ):
  if w.count( 'Е' ) == 2:
    k += 1

print( k )

k = len( [w for w in product('СТЕПАН', repeat=6)
                if w.count( 'Е' ) == 2 ] )
print( k )

print( len( [w for w in product('СТЕПАН', repeat=6)
               if w.count('Е') == 2 ] ) )

print( sum( 1 for w in product('СТЕПАН', repeat=6)
              if w.count('Е') == 2 ) )

print( sum( w.count('Е') == 2
            for w in product('СТЕПАН', repeat=6) ) )
