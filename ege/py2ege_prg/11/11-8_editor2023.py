"""
(Демо-2023) Дана программа для Редактора:
НАЧАЛО
ПОКА нашлось (>1) ИЛИ нашлось (>2) ИЛИ нашлось (>0)
  ЕСЛИ нашлось (>1)
    ТО заменить (>1, 22>)
  КОНЕЦ ЕСЛИ
  ЕСЛИ нашлось (>2)
    ТО заменить (>2, 2>)
  КОНЕЦ ЕСЛИ
  ЕСЛИ нашлось (>0)
    ТО заменить (>0, 1>)
  КОНЕЦ ЕСЛИ
КОНЕЦ ПОКА
КОНЕЦ
На вход приведённой выше программе поступает строка, начинающаяся с символа
«>», а затем содержащая 39 цифр «0», n цифр «1» и 39 цифр «2», расположенных
в произвольном порядке. Определите наименьшее значение n, при котором
сумма числовых значений цифр строки, получившейся в результате выполнения
программы, является простым числом.
"""
def alg( s ):
  while ">1" in s or ">2" in s or ">0" in s:
    if ">1" in s:
      s = s.replace( ">1", "22>", 1 )
    if ">2" in s:
      s = s.replace( ">2", "2>", 1 )
    if ">0" in s:
      s = s.replace( ">0", "1>", 1 )
  return s

def isPrime( n ):
  return n > 1 and \
         all( n % d != 0
              for d in range(2,round(n**0.5)+1) )

#------------------------------

n = 0
while True:
  s = alg( '>' + 39*'0' + n*'1' + 39*'2' )
  sumDigits = sum( map(int, s[:-1]) )
  if isPrime( sumDigits ):
    break
  n += 1

print( n, sumDigits )

#------------------------------

for n in range(0,1000):
  s = alg( '>' + 39*'0' + n*'1' + 39*'2' )
  sumDigits = sum( map(int, s[:-1]) )
  if isPrime( sumDigits ):
    break
  n += 1

print( n, sumDigits )

#------------------------------
for n in range(0,1000):
  s = '>' + 39*'0' + n*'1' + 39*'2'
  while ">1" in s or ">2" in s or ">0" in s:
    if ">1" in s:
      s = s.replace( ">1", "22>", 1 )
    if ">2" in s:
      s = s.replace( ">2", "2>", 1 )
    if ">0" in s:
      s = s.replace( ">0", "1>", 1 )
  sumDigits = sum( map(int, s[:-1]) )
  if isPrime( sumDigits ):
    break

print( n, sumDigits )

#------------------------------

print( min( n for n in range(1,100)
       if isPrime( sum( map(int,
         alg( '>'+39*'0'+n*'1'+39*'2' )[:-1]) ) ) ) )

