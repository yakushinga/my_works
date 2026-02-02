N = 10000
from random import randint, choice

with open('data10-4.txt', 'w') as F:
  for _ in range(N):
    while True:
      n = randint( -10000, 10000 )
      if n <= 7538 or '5' not in str(n):
        break
    print( n, file = F )
