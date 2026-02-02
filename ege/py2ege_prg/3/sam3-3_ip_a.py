"""
Узел с IP-адресом 63.254.104.115 принадлежит сети с маской 255.255.А.0, где
А — некоторое допустимое для записи маски число. Определите минимальное значение
А, при котором для всех IP-адресов этой сети в двоичной записи IP-адреса
суммарное количество единиц в левых двух байтах не меньше суммарного
количества единиц в правых двух байтах.
"""
from ipaddress import ip_network

hostIP = '63.254.104.115'
allA = [0, 128, 192, 224, 240, 248, 252, 254, 255]
left1 = f'{63:b}{254:b}'.count('1')

def valid( net ):
  for ip in net:
    if left1 < f'{ip:b}'[16:].count('1'):
      return False
  return True

for A in allA:
  net = ip_network(f'{hostIP}/255.255.{A}.0',0)
  if valid( net ):
    print( A )
    break

print('------------------------------')

hostIP = '63.254.104.115'
allA = [0, 128, 192, 224, 240, 248, 252, 254, 255]
left1 = f'{63:b}{254:b}'.count('1')
for A in allA:
  net = ip_network(f'{hostIP}/255.255.{A}.0',0)
  for ip in net:
    if left1 < f'{ip:b}'[16:].count('1'):
      break
  else:
    print( A )
    break
