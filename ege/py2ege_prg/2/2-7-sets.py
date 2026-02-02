def F( A, x ):
  return (x not in A) <= ((x not in Q) <= (x not in P))

def valid( A ):
  for x in range(0, 8):
    if not F(A, x): return False
  return True

def valid( A ):
  return all( F(A, x) for x in range(0, 8) )

P = { 1, 2, 3, 4 }
Q = { 3, 4, 5, 6 }

A = P | Q
for a in P | Q:
  if valid(A-{a}):
    A.remove( a )

p = 1
for x in A: p *= x
print( A, p )

A = P | Q
for a in P | Q:
  if all( F(A-{a}, x) for x in range(0, 8) ):
    A.remove( a )

p = 1
for x in A: p *= x
print( A, p )
