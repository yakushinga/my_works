from random import randint, shuffle

MAXTIME = 365*24*60*60

with open('26-181.txt') as F:
  N = int(F.readline())
  events = { 0: 0 }
  for i in range(N):
    k, start, end = map(int, F.readline().split())
    events[start] = events.get( start, 0 ) + 1
    events[end] = events.get( end, 0 ) - 1

events[MAXTIME] = 1
events[0] = -1
events = sorted( ((t,count) for t, count in events.items() if count != 0),
                 key = lambda x: abs(x[0]) )

active = 0
total = 0
twoCellsCount = 0
for i in range(1,len(events)):
  t, count = events[i]
  if active == 2:
    total += t - abs(events[i-1][0])
    #print( abs(events[i-1][0]), t )
    twoCellsCount += 1
  active += count

print( twoCellsCount, total )

