"""
Кузьма составляет шестибуквенные слова из букв слова БОБЫЛЬ. Он выбирает
только слова, в которых буква Ь не стоит на первом месте и после гласной.
Сколько таких слов может составить Кузьма?
(Ответ: 7782)
"""
from itertools import product

count = 0
for w in product('БОЫЛЬ', repeat=6):
   s = ''.join(w)
   if s[0] != 'Ь' and 'ОЬ' not in s and 'ЫЬ' not in s:
      count += 1

print( count )

#----------------------------------------

count = 0
for w in set(product('БОБЫЛЬ', repeat=6)):
   s = ''.join(w)
   if s[0] != 'Ь' and 'ОЬ' not in s and 'ЫЬ' not in s:
      count += 1

print( count )
