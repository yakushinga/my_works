"""
В файле input.txt в столбик записаны натуральные числа, не превышающие 10 000;
их количество неизвестно.  Найдите максимальное из чисел, оканчивающихся на 32.
Гарантируется, что в файле есть хотя бы одно число, оканчивающееся на 32.
"""
max32 = 0
for s in open("i/input_4.txt") :
  n = int( s )
  if n % 100 == 32 and n > max32:
    max32 = n

print( max32 )

#----------------------------

data = [ int(s) for s in open("i/input_4.txt") ]
data32 = [ n for n in data if n % 100 == 32 ]
print( max(data32) )

#----------------------------

data32 = [ n for s in open("i/input_4.txt")
           if (n := int(s)) % 100 == 32 ]
print( max(data32) )

#----------------------------

print( max( n for s in open("i/input_4.txt")
              if (n := int(s)) % 100 == 32 ) )
