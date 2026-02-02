def horner( digits, base ):
  n = 0
  for d in digits:
    n = n*base + d
  return n

def digits2int( digits, base ):
  n, power = 0, len(digits)-1
  for d in digits:
    n += d*base**power
    power -= 1
  return n

def digits2int( digits, base ):
  n = 0
  for power, d in enumerate(digits[::-1]):
    n += d*base**power
  return n

def digits2int( digits, base ):
  return sum( d*base**power
              for power, d in enumerate(digits[::-1]) )

c = [11, 2, 12, 3]
print( horner(c, 16) )
print( digits2int(c, 16) )