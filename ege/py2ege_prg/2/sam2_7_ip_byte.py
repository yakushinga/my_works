"""
Для узла с IP-адресом 115.98.181.167 адрес сети равен 115.98.181.160. Определите
наименьшее возможное значе-ние последнего (самого правого) байта маски.
(Ответ: 224)
"""
from ipaddress import ip_network
def valid( b ):
  hostIP = "115.98.181.167"
  netIP = "115.98.181.160"
  net = ip_network(
        f"{hostIP}/255.255.255.{b}", 0 )
  return str(net.network_address) == netIP

bAll = [0, 128, 192, 224, 240, 248,
        252, 254, 255]
for b in bAll:
  if valid(b) :
    print( b )
    break

print( '----------------------' )

bAll = [0, 128, 192, 224, 240, 248,
        252, 254, 255]
for b in bAll:
  if 167 & b == 160 :
    print( b )
    break

print( '----------------------' )

bAll = [0, 128, 192, 224, 240, 248,
        252, 254, 255]
print( min( b for b in bAll
            if 167 & b == 160 ) )


