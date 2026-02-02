"""
(Демо-2024) В терминологии сетей TCP/IP маской сети называют двоичное число, которое
показывает, какая часть IP-адреса узла сети относится к адресу сети, а какая –
к адресу узла в этой сети. Адрес сети получается в результате применения
поразрядной конъюнкции к заданному адресу узла и маске се-ти. Сеть задана
IP-адресом 192.168.32.160 и маской сети 255.255.255.240. Сколько в этой сети
IP-адресов, для которых сумма единиц в двоичной записи IP-адреса чётна?
"""
def ip2int( s ):
  sBin = ''
  for p in s.split('.'):
    sBin += f"{int(p):08b}"
  return int( sBin, 2 )

ip2int( "192.168.32.160" )

def ip2int( s ):
  return int( ''.join( f"{int(p):08b}" for p in s.split('.') ), 2 )

def ip2int( s ):
  ip = 0
  for p in s.split('.'):
    ip = ip*256 + int(p)
  return ip

print( ip2int( "192.168.32.160" ) )

def ip2int( s ):
  n = [ int(p) for p in s.split('.') ]
  return n[0]*256**3 + n[1]*256**2 + n[2]*256 + n[3]

print( ip2int( "192.168.32.160" ) )

net = ip2int( "192.168.32.160" )
mask = ip2int( "255.255.255.240" )
zeros = f"{mask:032b}".count('0')

count = 0
for i in range(2**zeros):
  #if f"{net+i:032b}".count('1') % 2 == 0:
  if f"{net+i:b}".count('1') % 2 == 0:
    count += 1
print( count )

print( '----------------------' )

print( len( [ i for i in range(2**zeros)
              if f"{net+i:b}".count('1') % 2 == 0 ] ) )

print( '----------------------' )

print( sum( f"{net+i:032b}".count('1') % 2 == 0
            for i in range(2**zeros) ) )

print( '----------------------' )

from ipaddress import ip_network
net = ip_network('192.138.32.160/255.255.255.240')
count = 0
for ip in net:
  if f"{ip:b}".count('1') % 2 == 0:
    count += 1
print( count )

print( '----------------------' )

print( sum( f"{ip:b}".count('1') % 2 == 0
       for ip in net ) )
