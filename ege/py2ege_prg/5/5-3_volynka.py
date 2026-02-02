"""
Все пятибуквенные слова, составленные из букв В, О, Л, Ы, Н, К, А, записаны в
алфавитном порядке и пронумерованы начиная с 1. Начало списка выглядит так:
1. ААААА
2. ААААВ
3. ААААК
4. ААААЛ
5. ААААН
...
Под каким номером стоит последнее слово, в котором буква А встречается не менее
двух раз, буква Ы не стоит в начале слова, а вторая с конца буква – К?
"""
from itertools import product

i = 1
for w in product(sorted('ВОЛЫНКА'), repeat=5):
  if w.count('А') >= 2 and w[0] != 'Ы' and w[-2] == 'К':
    if i > 14000:
      print( i, ''.join(w) )
  i += 1

#---------------------------------------------

for i, w in enumerate(
              product(sorted('ВОЛЫНКА'), repeat=5) ):
  if w.count('А') >= 2 and w[0] != 'Ы' and w[-2] == 'К':
    if i > 14000:
      print( i+1, ''.join(w) )

#---------------------------------------------

for i, w in enumerate(
              product(sorted('ВОЛЫНКА'), repeat=5), start=1 ):
  if w.count('А') >= 2 and w[0] != 'Ы' and w[-2] == 'К':
    if i > 14000:
      print( i, ''.join(w) )

#---------------------------------------------

i = 7**5
for w in product(sorted('ВОЛЫНКА', reverse=True), repeat=5):
  if w.count('А') >= 2 and w[0] != 'Ы' and w[-2] == 'К':
    print( i, ''.join(w) )
    break
  i -= 1

#---------------------------------------------

for i, w in enumerate(
        product(sorted('ВОЛЫНКА', reverse=True), repeat=5) ):
  if w.count('А') >= 2 and w[0] != 'Ы' and w[-2] == 'К':
    print( 7**5 - i, ''.join(w) )
    break
