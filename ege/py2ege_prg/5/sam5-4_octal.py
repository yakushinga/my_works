"""
Сколько существует чисел, восьмеричная запись которых состоит из четырёх
различных цифр, расположенных в порядке возрастания?
(Ответ: 35)
"""
from itertools import product

count = 0
for w in product('01234567', repeat=4):
  if w[0] != '0' and  w[0] < w[1] < w[2] < w[3]:
    count += 1

print( count )

#----------------------------------------

from itertools import permutations
count = 0
for w in permutations('01234567', 4):
  if w[0] != '0' and  w[0] < w[1] < w[2] < w[3]:
    count += 1

print( count )
