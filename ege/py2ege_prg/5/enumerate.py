words = ['айва', 'слива', 'яблоко']

for i in range(len(words)):
  print( i+1, words[i] )

print('--------------------------------')

for i, w in enumerate(words):
  print( i+1, w )

print('--------------------------------')

for i, w in enumerate(words, start=1):
  print( i, w )

