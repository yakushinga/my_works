from random import *
import string

N = 1_000_000

s = ''
while len(s) < N:
  if randint(1, 100) < 5:
    s += 'SNOW'
  else:
    s += choice( string.ascii_uppercase )

f = open('data11-20.txt', 'w')
f.write( s[:N] )
f.close()