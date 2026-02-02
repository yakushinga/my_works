"""
Для узла с IP-адресом 115.98.181.167 адрес сети равен 115.98.181.160. Определите
наименьшее возможное значение последнего (самого правого) байта маски.
"""
bMaskAll = [0, 128, 192, 224, 240, 248, 252, 254, 255]

for b in bMaskAll:
  if 167 & b == 160:
    print( b )
    break

print('----------------------------------')

print( min( b for b in bMaskAll if 167 & b == 160 ) )

print('----------------------------------')

from ipaddress import ip_network
netIP = '115.98.181.160'
hostIP = '115.98.181.167'
bMaskAll = [0, 128, 192, 224, 240, 248, 252, 254, 255]
for b in bMaskAll:
  net = ip_network( f'{hostIP}/255.255.255.{b}', 0 )
  if str(net.network_address) == netIP:
    print( b )
    break

print('----------------------------------')

from ipaddress import ip_network
netIP = '115.98.181.160'
hostIP = '115.98.181.167'
for ones in range(32):
  net = ip_network( f'{hostIP}/{ones}', 0 )
  if str(net.network_address) == netIP:
    print( ones )
    break

print('----------------------------------')

bMaskAll = [0, 128, 192, 224, 240, 248, 252, 254, 255]
print( min( 24+i for i, b in enumerate(bMaskAll)
                 if 167 & b == 160 ) )

