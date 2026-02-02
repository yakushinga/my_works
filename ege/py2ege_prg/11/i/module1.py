from random import *
import string

N = 1000_000
f = open('input_17.txt', 'w')

s = ''
while len(s) < N:
  s += choice(string.ascii_uppercase+string.digits)

f.write( s[:N] )
f.close()