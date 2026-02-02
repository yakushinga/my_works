"""
(Е. Джобс) Текстовый файл data13-5.txt состоит не более чем из 10^6 символов
X, Y, Z. Определите максимальную длину подстроки, которая состоит из
сочетаний XY, YZ, YZZ, записанных в произвольном порядке.
(Ответ: 94)
"""
s = open('data/data13-5.txt').readline()

patterns = ['XY', 'YZ', 'YZZ']

count = [0]*len(s)
for i in range(1, len(s)):
  newCount = 0
  if s[i-1:i+1] in patterns:
    newCount = count[i-2] + 2
  if s[i-2:i+1] in patterns:
    newCount = max( count[i-3] + 3, newCount )
  count[i] = newCount

print( max(count) )

print('---------------------------------')

s = open('data/data13-5.txt').readline()

patterns = ['XY', 'YZ', 'YZZ']

def find( s, i ):
  maxLen = 0
  if s[i:i+2] in patterns:
    maxLen = 2 + find(s,i+2)
  if s[i:i+3] in patterns:
    maxLen = max( 3 + find(s,i+3), maxLen )
  return maxLen

print( max( find(s,i)
            for i in range(len(s)) ) )

