"""
В файле data12-5.txt содержатся сведения о въезде автомобилей на парковку
бизнес-центра и выезде из неё.  В первой строке входного файла находится
натуральное число N – количество записей о движении автомобилей. Следующие
N строк содержат пары чисел, обозначающих время въёзда автомобиля на парковку
и время выезда с неё (в минутах от начала суток). Считается, что в минуту
въезда и в минуту выезда автомобиль находится на стоянке. Определите наибольшее
количество автомобилей, которые находились на парковке одновременно, и
количество пиков, когда их количество было наибольшим (пик может продолжаться
несколько минут).
(Ответ: 60 4)
"""
with open("data/data12-5.txt") as F:
  N = int( F.readline() )
  data = []
  for s in F:
    t0, t1 = map( int, s.split() )
    data.append( t0 )      # въезд
    data.append( -(t1+1) ) # выезд

data.sort( key = abs )

count = peakValue = numPeaks = 0
lastPeak = -100   # пиков ещё не было
for t in data:
  if t >= 0: # въезд
    count += 1
    if count > peakValue:
      peakValue = count
      numPeaks, lastPeak = 1, t
      #print( t, count, numPeaks )
    elif count == peakValue:
      numPeaks += (t > lastPeak+1)
      #print( t, count, numPeaks )
      lastPeak = t
  else: # выезд
    count -= 1
print( peakValue, numPeaks  )

