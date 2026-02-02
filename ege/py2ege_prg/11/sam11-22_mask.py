"""
Среди натуральных чисел, не превышающих 10^8, найдите все числа,
соответствующие маске 1*2??76, делящиеся на 1923 без остатка.
(Ответ: 10022676 5212, 12522576 6512, 15022476 7812,
17522376 9112, 19829976 10312)
"""
from itertools import product

digits = '0123456789'
for L in range(0,3):
  for z in product(digits, repeat=L):
    for x, y in product(digits, repeat=2):
      z = ''.join( z )
      n = int( f"1{z}2{x+y}76" )
      if n % 1923 == 0:
        print( n, n//1923 )


