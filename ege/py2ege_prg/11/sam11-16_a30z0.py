"""
Текстовый файл data11-12.txt состоит не более чем из 10^6 заглавных латинских
букв. Определите минимальную длину подстроки, в которой символ A встречается
не менее 30 раз, а символ Z не встречается совсем.
(Ответ: 507)
"""
s = open("data/data11-12.txt").read()

#s = "NAZAKLALA"

NA = 30
NZ = 0

def valid():
  return countA <= NA and countZ <= NZ

countA = countZ = 0
minLen = 10**10
L = 0
for R in range(len(s)):
   countA += (s[R] == 'A')
   countZ += (s[R] == 'Z')
   while countA - (s[L] == 'A') >= NA or countZ > NZ:
     countA -= (s[L] == 'A')
     countZ -= (s[L] == 'Z')
     L += 1
   #print( L, R, s[L:R+1], countA, countZ )
   if countA >= NA and countZ <= NZ:
     minLen = min( R-L+1, minLen )

print( minLen )

print("----------------------------------")

N = len(s)
minLen = 10**10
for L in range(N):
  countA = countZ = 0
  for R in range(L, N):
    if s[R] == 'A': countA += 1
    if s[R] == 'Z': countZ += 1
    if countA >= NA and countZ <= NZ:
      minLen = min( R-L+1, minLen )

print( minLen )

