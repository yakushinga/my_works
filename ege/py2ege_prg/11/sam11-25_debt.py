"""
(Демо-2023) Определите, сколько раз в тексте файла data10-2.txt встречается
слово «долг» или «Долг». Другие формы слова «долг», такие как «долги»,
«долгами» и т. д., учитывать не следует.
(Ответ: 1)
"""
s = open("data/data10-2.txt", encoding='cp1251').read()

import re
mWord = re.findall( r'\bдолг\b', s, re.I )
print( len(mWord) )

#----------------------------------------------

s = open("data/data10-2.txt", encoding='cp1251').read()
s = s.lower()
s = ' ' + s + ' '

letters = 'абвгдеёжзиклмнопрстуфхцчшщъыьэюя'
count = 0
for i in range(len(s)):
  if s[i:i+4] == 'долг' and \
     (s[i-1] not in letters and s[i+4] not in letters):
     count += 1
print( count )

