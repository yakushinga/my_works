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
                 key = lambda x: x[0] )

active = 0
maxInterval = 0
activityCount = 0
for i in range(1,len(events)):
  t, count = events[i]
  if active == 0:
    tStart = t
  active += count
  if active == 0:
    maxInterval = max( t - tStart, maxInterval )
    #print( tStart, t )
    activityCount += 1

print( activityCount, maxInterval )

