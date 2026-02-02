"""
Определите, сколько раз в тексте файла input.txt встречается сочетание букв
«все» или «Все» только в составе других слов, но не как отдельное слово.
В ответе укажите только число.
"""
s = open("i/input_2.txt", encoding='cp1251').read()
s = s.lower()
s = ' ' + s + ' '

letters = 'абвгдеёжзиклмнопрстуфхцчшщъыьэюя'
count = 0
for i in range(1,len(s)-3):
  if s[i:i+3] == 'все' and \
     (s[i-1] in letters or s[i+3] in letters):
     count += 1
print( count )

#-----------------------------------------

s = open("i/input_2.txt", encoding='cp1251').read().lower()
import re
m = re.findall( 'все', s, re.I )
mWord = re.findall( r'\bвсе\b', s, re.I )
print( len(m) - len(mWord) )

#-----------------------------------------

s = open("i/input_2.txt", encoding='cp1251').read()
s = ' ' + s.lower() + ' '
for before in ' "(':
  for after in ' .,;:!?)"':
    s = s.replace( f'{before}все{after}', ' ' )
print( s.count('все') )

