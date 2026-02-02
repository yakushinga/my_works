"""
Определите, сколько раз в тексте файла data10-2.txt встречается
отдельное слово «и» или «И». Буквы "и" в составе других слов учитывать не следует.
(Ответ: 157)
"""

cnt = 0
for s in open("data/data10-2.txt", encoding='cp1251'):
  s = s.lower().replace(',',' ').replace('(',' ').replace('"',' ')
  s = ' ' + s + ' '
  cnt += s.count(" и ")

print( cnt )

#--------------------------------------------------------------

cnt = 0
for s in open("data/data10-2.txt", encoding='cp1251'):
  s = s.lower().replace(',',' ').replace('(',' ').replace('"',' ')
  if s:
    cnt += s.count(" и ")
    cnt += (s == 'и')
    if len(s) > 1:
      cnt += (s[0] == 'и' and s[1] in " \n")

print( cnt )

#--------------------------------------------------------------

import re
s = open("data/data10-2.txt", encoding='cp1251').read()
parts = re.findall( r'\bи\b', s, re.I )
print( len(parts) )

