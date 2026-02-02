"""
Обозначим через ДЕЛ(n, m) утверждение «натуральное число n делится без остатка
на натуральное число m». Для ка-кого наименьшего натурального числа А формула
ДЕЛ(A, 9) ∧ (ДЕЛ(280, x) → (¬ДЕЛ(A, x) → ¬ДЕЛ(730, x)))
тождественно истинна, т. е. принимает значение 1 при любом натуральном
значении переменной х?
(Ответ: 90)
"""
def ДЕЛ( n, d ):
  return n % d == 0

def f( x, A ):
  return (ДЕЛ(A, 9) and (ДЕЛ(280, x)) <= ((not ДЕЛ(A, x)) <= (not ДЕЛ(730, x))))

for A in range(1,1000):
  OK = True
  for x in range(1, 1000):
    if not f(x, A):
      OK = False
      break
  if OK:
    print( A )
    break

for A in range(1,1000):
  if all( f(x, A) for x in range(1,1000) ):
    print( A )
    break

print( min( A for A in range(1,1000)
              if all( f(x, A) for x in range(1,1000) ) ) )