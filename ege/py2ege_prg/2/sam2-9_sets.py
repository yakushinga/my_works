"""
Элементами множеств А, P и Q являются натуральные числа,
причём P = { 1, 2, 3, 4 } и Q = { 3, 4, 5, 6 }. Известно, что выра-
жение
  ¬(x ∈ A) → (¬(x ∈ Q) → ¬(x ∈ P))
истинно (т. е. принимает значение 1) при любом значении пе-
ременной х. Определите наименьшее возможное произведение
элементов множества A.
(Ответ: 2)
"""
def F( A, x ):
  return (x not in A) <= ((x not in Q) <= (x not in  P))
  return (x in A) or (x in Q) or (x not in P)

def valid( A ):
  for x in range(0, 8):
    if not F(A, x):
      print( '#', x, A, x in A, x in P, x not in Q )
      return False
  return True

#def valid( A ):
#  return all( F(A, x) for x in range(0, 8) )

P = { 1, 2, 3, 4 }
Q = { 3, 4, 5, 6 }

A = P | Q
for a in P | Q:
  if valid(A-{a}):
    A.remove( a )

print( len(A), A )

print('-----------------------------------------')

A = P | Q
for a in P | Q:
  if all( F(A-{a}, x) for x in range(0, 8) ):
    A.remove( a )

print( len(A), A )
