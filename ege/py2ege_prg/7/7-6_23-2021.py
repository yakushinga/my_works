"""
Исполнитель преобразует число на экране. У исполнителя есть две команды,
которым присвоены номера:
  1. Прибавить 1
  2. Умножить на 2
Первая команда увеличивает число на экране на 1, вторая умножает его на 2.
Программа для исполнителя – это последовательность команд. Сколько существует
программ, для которых при исходном числе 1 результатом является число 20, и
при этом траектория вычислений содержит число 10?
"""
def F( n, end ):
  return 1 if n == end else \
         0 if n > end else \
         F( n+1, end ) + F( 2*n, end )

print( F(1, 10)*F(10, 20) )

# ---------------------------------

def F( n, end, path = [] ):
  if n == end: return 10 in path
  if n > end: return 0
  path = path + [n]   # создаётся новый список!
  # path += [n]       !!! это неверный вариант
  # path.append( n )  !!! это неверный вариант
  return F( n+1, end, path ) + F( 2*n, end, path )

print( F(1, 20) )

# ---------------------------------

def F( n, end, hit10 = 0 ):
  if n == end: return hit10
  if n > end: return 0
  if n == 10: hit10 = 1
  return F( n+1, end, hit10 ) + F( 2*n, end, hit10 )

print( F(1, 20) )

# ---------------------------------

def F( n, end, points = set() ):
  if n == end: return len(points) == 2
  if n > end: return 0
  if n in [10, 15]: points = points | {n}
  return F( n+1, end, points ) + F( 2*n, end, points )

print( F(1, 20) )