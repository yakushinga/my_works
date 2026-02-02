"""
Для узла с IP-адресом 211.15.200.203 адрес сети равен 211.15.200.192. Определите
наибольшее возможное значение последнего (самого правого) байта маски.
Ответ: 240
"""
bMaskAll = [0, 128, 192, 224, 240, 248, 252, 254, 255]

for b in bMaskAll:
  if 203 & b == 192:
    print( b )

print('----------------------------------')

print( max( b for b in bMaskAll if 203 & b == 192 ) )

print('----------------------------------')

from ipaddress import ip_network
netIP = '211.15.200.192'
hostIP = '211.15.200.203'
bMaskAll = [0, 128, 192, 224, 240, 248, 252, 254, 255]
for b in bMaskAll:
  net = ip_network( f'{hostIP}/255.255.255.{b}', 0 )
  if str(net.network_address) == netIP:
    print( b )

print('----------------------------------')

from ipaddress import ip_network
netIP = '211.15.200.192'
hostIP = '211.15.200.203'
for ones in range(32):
  net = ip_network( f'{hostIP}/{ones}', 0 )
  if str(net.network_address) == netIP:
    print( ones )

print('----------------------------------')

bMaskAll = [0, 128, 192, 224, 240, 248, 252, 254, 255]
print( max( 24+i for i, b in enumerate(bMaskAll)
                 if 203 & b == 192 ) )

