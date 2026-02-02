def sys15( n ):
  alphabet = '0123456789ABCDE'
  s = ''
  while n:
    s = alphabet[n%15] + s
    n //= 15
  return s

for i in range(1, 1000):
  if i != int( sys15(i), 15 ):
    print( i )