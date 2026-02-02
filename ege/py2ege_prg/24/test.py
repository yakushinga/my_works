from time import time

glas = "АЕЁИОУЫЭЮЯ"
sogl = "БВГДЖЗЙКЛМНПРСТФХЧЦШЩ"

s = open("data.txt").readline()

start = time()
state, count = 1, 0
for c in s:
  if state == 1:
    if c in glas: # переход 1-> 2
      state = 2
  else:
    if c in sogl: # переход 2-> 1
      state = 1
      count += 1
delta1 = time() - start
print( count )
print( delta1 )

from itertools import product
start = time()
count = 0
for p in product(glas, sogl):
   count += s.count( "".join(p) )
delta2 = time() - start
print( count )
print( delta2 )
