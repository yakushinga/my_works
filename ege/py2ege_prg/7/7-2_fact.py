"""
(Демо-2023) Алгоритм вычисления значения функции F(n), где n – натуральное число, задан
следующими соотношениями:
F(n) = 1 при n = 1;
F(n) = n· F(n − 1) при n > 1.
Чему равно значение функции F(2023) / F(2020)?
"""
import sys

sys.setrecursionlimit( 2500 )

def F( n ):
  return 1 if n == 1 else  n*F(n-1)

print( F(2023) // F(2020) )

def F( n ):
  r = 1
  for i in range(2,n+1):
    r *= i
  return r

print( F(2023) // F(2020) )

print( 2023*2022*2021 )

