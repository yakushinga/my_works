"""
Узел с IP-адресом 64.32.А.153, где А — некоторое допустимое для записи
IP-адреса число, принадлежит сети с маской 255.255.224.0. Определите минимальное
начение А, при котором для всех IP-адресов этой сети в двоичной записи
IP-адреса суммарное количество единиц в левых двух байтах не больше
суммарного количества единиц в правых двух байтах.
"""
import timeit
from ipaddress import ip_network

def valid( net ):
  mask = '255.255.224.0'
  net = ip_network(f'64.32.{A}.153/{mask}', 0)
  for ip in net:
    s = f'{ip:b}'
    if s[:16].count('1') > s[16:].count('1'):
      return False
  return True

t0 = timeit.default_timer()
for A in range(256):
  if valid( A ):
    print( A )
    break

print( timeit.default_timer() - t0 )

print( '--------------------------' )
t0 = timeit.default_timer()
mask = '255.255.224.0'
for A in range(256):
  net = ip_network(f'64.32.{A}.153/{mask}', 0)
  for ip in net:
    s = f'{ip:b}'
    if s[:16].count('1') > s[16:].count('1'):
      break
  else:
    print( A )
    break

print( timeit.default_timer() - t0 )

print( '--------------------------' )

t0 = timeit.default_timer()
for A in range(256):
  net = ip_network(f'64.32.{A}.153/{mask}', 0)
  if all( (s := f'{ip:b}')[:16].count('1') <= s[16:].count('1')
          for ip in net ):
    print( A )
    break

print( timeit.default_timer() - t0 )

print( '--------------------------' )

def ip2int( s ):
  ip = 0
  for p in s.split('.'):
    ip = ip*256 + int(p)
  return ip

t0 = timeit.default_timer()
mask = ip2int("255.255.224.0")
zeros = f"{mask:b}".count('0')
for A in range(256):
  A = 96
  net = ip2int(f"64.32.{A}.153") & mask
  for i in range(2**zeros):
    s = f"{net+i:b}"
    if s[:16].count('1') > s[16:].count('1'):
       break
  else:
    print( A )
    break

print( timeit.default_timer() - t0 )


print( '--------------------------' )

def ip2int( s ):
  ip = 0
  for p in s.split('.'):
    ip = ip*256 + int(p)
  return ip

t0 = timeit.default_timer()

def valid( A ):
  mask = ip2int("255.255.224.0")
  zeros = f"{mask:b}".count('0')
  net = ip2int(f"64.32.{A}.153") & mask
  count = 0
  for i in range(2**zeros):
    s = f"{net+i:b}"
    if s[:16].count('1') <= s[16:].count('1'):
       count += 1
  return count == 2**zeros

for A in range(256):
  if valid( A ):
    print( A )
    break

print( timeit.default_timer() - t0 )
