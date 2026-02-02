"""
Введём выражение M & K, обозначающее поразрядную конъюнкцию M и K (логическое
«И» между соответствующими битами двоичной записи). Определите наименьшее
натуральное число A, такое что выражение
(x & 49 ≠ 0) → ((x & 33 = 0) → (x & A ≠ 0))
тождественно истинно, т. е. принимает значение 1 при любом натуральном значении
переменной x?
(Ответ: 16)
"""
def f(x, A):
  return (x & 49 != 0) <= ((x & 33 == 0) <= (x & A != 0))

for A in range(1, 100):
  OK = True
  for x in range(1, 1000):
    if not f(x, A):
      OK = False
      break
  if OK:
    print( A )
    break

for A in range(1, 100):
  if all( f(x, A) for x in range(1,1000) ):
    print( A )
    break

print( min( A for A in range(1,100)
              if all( f(x, A) for x in range(1,1000) ) ) )