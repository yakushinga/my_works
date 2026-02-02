"""
Два узла, находящиеся в одной сети, имеют IP-адреса 121.171.15.70 и 121.171.3.68.
Укажите наибольшее возможное значение третьего слева байта маски сети.
(Ответ: 240)
"""

for b in [ 256-2**i for i in range(0,9) ]:
  if (15 & b) == (3 & b):
    print( b )

print('----------------------')

from ipaddress import ip_network, IPv4Address

def valid ( b ):
  net = ip_network(f'121.171.15.70/255.255.{b}.0', 0)
  return IPv4Address('121.171.3.68') in net

for b in [ 256-2**i for i in range(0,9) ]:
  if valid( b ):
    print( b )


