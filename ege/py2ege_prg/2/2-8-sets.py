def F( A, x ):
  return ((x in A) <= (x in P)) or \
         ((x not in Q) <= (x not in A))

def valid( A ):
  for x in range(0, 8):
    if not F(A, x): return False
  return True

def valid( A ):
  return all( F(A, x) for x in range(0, 8) )

P = { 1, 2, 3, 4 }
Q = { 3, 4, 5, 6 }

A = set()
for a in P | Q:
  if valid( A | {a}):
    A.add( a )

print( A, sum(A) )

print('--------------------------')

P = { 1, 2, 3, 4 }
Q = { 3, 4, 5, 6 }

A = set()
for a in P | Q:
  if all( F(A | {a}, x) for x in range(0, 8) ):
    A.add( a )

print( A, sum(A) )
