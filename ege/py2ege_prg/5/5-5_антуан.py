"""
Антуан составляет все возможные шестибуквенные слова из букв своего имени.
Каждая буква может входить в слово любое количество раз или не встречаться
совсем. Сколько Антуан может составить различных слов, в которых больше
 букв Н?
"""
from itertools import product

k = 0
for w in product( 'АНТУАН', repeat=6 ):
  if w.count('Н') > 2:
    k += 1

print( k, '!!! неверно !!!' )

k = 0
for w in set(product( 'АНТУАН', repeat=6 )):
  if w.count('Н') > 2:
    k += 1

print( k )

k = 0
for w in product( 'АНТУ', repeat=6 ):
  if w.count('Н') > 2:
    k += 1

print( k )

print( sum( 1 for w in product( 'АНТУ', repeat=6 )
              if w.count('Н') > 2  ) )

print( sum( w.count('Н') > 2
            for w in product( 'АНТУ', repeat=6 ) ) )