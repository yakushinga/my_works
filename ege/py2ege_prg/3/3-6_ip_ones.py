"""
Для узла с IP-адресом 193.57.165.211 адрес сети равен 193.57.160.0. Каково
наибольшее возможное количество единиц в разрядах маски?
"""
from ipaddress import ip_network

def valid( ones ):
  netIP = '193.57.160.0'
  hostIP = '193.57.165.211'
  net = ip_network( f'{hostIP}/{ones}', 0 )
  return str(net.network_address) == netIP

for ones in range(31,0,-1):
  if valid( ones ):
    print( ones )
    break

print( '--------------------' )

from ipaddress import ip_network
netIP = '193.57.160.0'
hostIP = '193.57.165.211'
for ones in range(31,0,-1):
  net = ip_network( f'{hostIP}/{ones}', 0 )
  if str(net.network_address) == netIP:
    print( ones )
    break

