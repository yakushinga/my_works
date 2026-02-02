"""
(Демо-2024) В каждой строке файла input.csv записано семь натуральных чисел,
разделённых точками с запятой. Определите количество строк таблицы, для
чисел которых выполнены оба условия:
– в строке есть два числа, каждое из которых повторяется дважды, остальные
  три числа различны;
– среднее арифметическое всех повторяющихся чисел строки меньше среднего
  арифметического всех её чисел.
"""
count = 0
for s in open("i/input_7.txt"):
  #data = list( map(int, s.split(';')) )
  data = [ int(p) for p in s.split(';') ]
  single, dup  = [], []
  for x in data:
    k = data.count( x )
    if k == 1:
       single.append( x )
    if k == 2:
       dup.append( x )
  if len(dup) == 4 and len(single) == 3 and \
     sum(dup)/4 < sum(data)/7:
     count += 1

print( count )

#---------------------------------------------

count = 0
for s in open("i/input_7.txt"):
  #data = list( map(int, s.split(';')) )
  data = [ int(p) for p in s.split(';') ]
  dup = [ x for x in data if data.count(x) == 2 ]
  single = [ x for x in data if data.count(x) == 1 ]
  if len(dup) == 4 and len(single) == 3 and \
     sum(dup)/4 < sum(data)/7:
     count += 1

print( count )
