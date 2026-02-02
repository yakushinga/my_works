"""
Текстовый файл data11-13.txt состоит не более чем из 10^6 заглавных латинских
букв. Определите максимальную длину подстроки, в которой символы
A, B и С встречается ровно по 2 раза.
(Ответ: 137)
"""
s = open("data/data11-13.txt").read()

def valid():
  return countA <= 2 and countB <= 2 and countC <= 2

countA = countB = countC = 0
maxLen = 0
L = 0
for R in range(len(s)):
   countA += (s[R] == 'A')
   countB += (s[R] == 'B')
   countC += (s[R] == 'C')
   while not valid():
     countA -= (s[L] == 'A')
     countB -= (s[L] == 'B')
     countC -= (s[L] == 'C')
     L += 1
   if countA == countB == countC == 2:
     maxLen = max( R-L+1, maxLen )

print( maxLen )

print("----------------------------------")

N = len(s)
maxLen = 0
for L in range(N):
  countA = countB = countC = 0
  for R in range(L, N):
    if s[R] == 'A': countA += 1
    if s[R] == 'B': countB += 1
    if s[R] == 'C': countC += 1
    if not valid(): break
    if countA == countB == countC == 2:
      maxLen = max( R-L+1, maxLen )

print( maxLen )

