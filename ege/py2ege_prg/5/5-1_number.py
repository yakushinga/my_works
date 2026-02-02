"""
Требуется определить номер заданного слова в отсортированном списке, который
хранится в переменной words.
"""
words = ['айва', 'слива', 'яблоко']

for i in range(len(words)):
  if words[i] == 'слива':
    print( i + 1 )
    break

print( list(enumerate(words)) )

for i, w in enumerate(words):
  if w == 'слива':
    print( i + 1 )
    break

for i, w in enumerate(words, start=1):
  if w == 'слива':
    print( i )
    break

print( words.index('слива') + 1 )