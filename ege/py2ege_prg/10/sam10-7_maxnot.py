"""
7. В каждой строке файла data10-7.csv записаны семь натуральных чисел,
разделённые точками с запятой. Определите сумму чисел в строке таблицы с
наименьшим номером, для которой выполнены оба условия:
– в строке есть два числа, которые повторяются дважды, остальные три числа различны;
– максимальное число строки не повторяется.
(Ответ: 261)
"""
for s in open("data/data10-7.csv"):
  data = list( map(int, s.split(';')) )
  dup = [ x for x in data if data.count(x) == 2 ]
  single = [ x for x in data if data.count(x) == 1 ]
  if len(dup) == 4 and max(data) not in dup:
     sumRow = sum( data )
     break

print( data )
print( sumRow )
