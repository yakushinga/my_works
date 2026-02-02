"""
Требуется определить количество слов в списке words, удовлетворяющих заданному
условию.
"""
words = ['A', 'B', 'A', 'C', 'A']

def valid( w ):
  return w == 'A'

count = 0
for w in words:
  if valid( w ):
    count += 1
print( count )


words = ['альфа', 'кара', 'кенгуру', 'суслик']

def valid( w ):
  return 'к' in w

count = 0
for w in words:
  if valid( w ):
    count += 1
print( count )
