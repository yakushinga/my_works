"""
Элина составляет все возможные пятибуквенные слова из букв Э, Л, И, Н, А. Каждая
буква может входить в слово любое количество раз или не встречаться совсем.
Сколько Элина может составить различных слов, в которых буквы Э и Л не стоят
рядом?
"""
from itertools import product

count = 0
for w in product( 'ЭЛИНА', repeat=5 ):
  s = ''.join( w )
  if 'ЭЛ' not in s and 'ЛЭ' not in s:
    count += 1

print( count )

count = len( [ s for w in product( 'ЭЛИНА', repeat=5 )
                if 'ЭЛ' not in (s:=''.join(w)) and 'ЛЭ' not in s ] )
print( count )

print( sum( 1 for w in product( 'ЭЛИНА', repeat=5 )
             if 'ЭЛ' not in (s:=''.join(w)) and 'ЛЭ' not in s ) )

print( sum( 'ЭЛ' not in (s:=''.join(w)) and 'ЛЭ' not in s
            for w in product( 'ЭЛИНА', repeat=5 )) )
