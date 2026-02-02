"""
Текстовый файл input.txt состоит не более чем из 10^6 символов X, Y, Z.
Определите максимальное количество идущих подряд троек символов ZXY, XYZ
или YZX.
"""
s = open('i/input_3.txt').readline()

count = [0]*len(s)
patterns = ['ZXY', 'XYZ', 'YZX']
for i in range(2, len(s)):
  if s[i-2:i+1] in patterns:
    if i == 2:
      count[i] = 1
    else:
      count[i] = count[i-3] + 1

print( max(count) )

print('---------------------------------')

s = open('i/input_3.txt').readline()

#s = "XZXYZYXYZYZXYZZ"

count = [0]*len(s)
patterns = ['ZXY', 'XYZ', 'YZX']
for i in range(2, len(s)):
  if s[i-2:i+1] in patterns:
    count[i] = count[i-3] + 1

print( max(count) )

print('---------------------------------')

s = open('i/input_3.txt').readline()

#s = "XZXYZYXYZYZXYZZ"

patterns = ['ZXY', 'XYZ', 'YZX']

def find( s, i ):
  if s[i:i+3] in patterns:
    return 1 + find(s,i+3)
  else:
    return 0

def find( s, i ):
  return 1 + find(s,i+3) \
           if s[i:i+3] in patterns else \
         0

maxLen = 0
for i in range(len(s)):
  maxLen = max( find(s,i), maxLen )
print( maxLen )

print( max( find(s,i)
            for i in range(len(s)) ) )

