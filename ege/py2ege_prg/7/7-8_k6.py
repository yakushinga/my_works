"""
Исполнитель преобразует число на экране. У исполнителя есть три команды,
которым присвоены номера:
  1. Прибавить 1
  2. Прибавить 2
  3. Умножить на 2
Первая команда увеличивает число на экране на 1, вторая – увеличивает на 2,
третья – умножает на 2. Программа для исполнителя – это последовательность
команд. Сколько существует программ, состоящих из 6 команд, для которых
при исходном числе 1 результатом является число 20?
"""
def F( n, end, k ):
  return 1 if n == end and k == 0 else \
         0 if n == end and k != 0 else \
         0 if n > end else \
         0 if n < end and k == 0 else \
         F( n+1, end, k-1 ) + F( n+2, end, k-1 ) \
                            + F( 2*n, end, k-1 )

print( F(1, 20, 6) )

#------------------------------

def F( n, end, k ):
  return int(k == 0) if n == end else \
         0 if n > end or k == 0 else \
         F( n+1, end, k-1 ) + F( n+2, end, k-1 ) \
                            + F( 2*n, end, k-1 )

print( F(1, 20, 6) )

#------------------------------

def F( n, end, k ):
  return k == 0 if n == end else \
         0 if n > end or k == 0 else \
         F( n+1, end, k-1 ) + F( n+2, end, k-1 ) \
                            + F( 2*n, end, k-1 )

print( F(1, 20, 6) )

#------------------------------
def F( n, end, prog ):
  return len(prog) == 6 if n == end else \
         0 if n > end else \
         F(n+1, end, prog+'1') + F(n+2, end, prog+'2') + \
         F(2*n, end, prog+'3')

print( F(1, 20, '') )

#------------------------------
def F( n, end, prog = '' ):
  return len(prog) == 6 if n == end else \
         0 if n > end else \
         F(n+1, end, prog+'1') + F(n+2, end, prog+'2') + \
         F(2*n, end, prog+'3')

print( F(1, 20) )
