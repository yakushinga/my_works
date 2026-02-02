"""
**Исполнитель преобразует число на экране. У исполнителя имеются четыре
команды, которым присвоены номера:
  1. Прибавить 1
  2. Прибавить 2
  3. Умножить на 2
  4. Умножить на 3
Выполняя первую из них, исполнитель увеличивает число на экране на 1, выполняя
вторую – увеличивает на 2, выполняя третью – умножает на 2, выполняя
четвёртую – умножает на 3. Сколько существует различных программ, преобразующих
число 1 в число 55555, которые не содержат ни двух подряд идущих команд
сложения, ни двух подряд идущих команд умножения?
(Ответ: 509)
"""

import timeit

def F( n, end, lastCmd = -1 ):
  if n == end: return 1
  if n > end: return 0
  count = 0
  if lastCmd != 1:
    count += F(n+1, end, 1) + F(n+2, end, 1)
  if lastCmd != 2:
    count += F(2*n, end, 2) + F(3*n, end, 2)
  return count

t0 = timeit.default_timer()
print( F(1, 55555), timeit.default_timer() - t0 )

#-----------------------------

def F( n, end, prog = '' ):
  if '++' in prog or '**' in prog: return 0
  return 1 if n == end else \
         0 if n > end else \
         F(n+1, end, prog+'+') + F(n+2, end, prog+'+') + \
         F(2*n, end, prog+'*') + F(3*n, end, prog+'*')

t0 = timeit.default_timer()
print( F(1, 55555), timeit.default_timer() - t0 )

