"""
Сеть задана IP-адресом 193.124.85.64 и маской сети 255.255.255.192. Сколько в
этой сети IP-адресов, для которых количество единиц в двоичной записи больше,
чем количество нулей?
(Ответ: 22)
"""
def ip2int( s ):
  sBin = ''
  for p in s.split('.'):
    sBin += f"{int(p):08b}"
  return int( sBin, 2 )

def ip2int( s ):
  return int( ''.join( f"{int(p):08b}" for p in s.split('.') ), 2 )

net = ip2int( "193.124.85.64" )
mask = ip2int( "255.255.255.192" )
zeros = f"{mask:b}".count('0')

count = 0
for i in range(2**zeros):
  s = f"{net+i:032b}"
  if s.count('1') > s.count('0'):
    count += 1
print( count )

print( '----------------------' )

print( len( [ i for i in range(2**zeros)
              if (s := f"{net+i:032b}").count('1') > s.count('0') ] ) )

print( '----------------------' )

print( sum( (s := f"{net+i:032b}").count('1') > s.count('0')
            for i in range(2**zeros) ) )

print( '----------------------' )

from ipaddress import ip_network
net = ip_network('193.124.85.64/255.255.255.192')
count = 0
for ip in net:
  s = f"{int(ip):032b}"
  if s.count('1') > s.count('0'):
    count += 1
print( count )
