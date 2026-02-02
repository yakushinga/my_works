"""
Для узла с IP-адресом 211.208.38.203 адрес сети равен 211.208.0.0. Каково
наименьшее возможное количество единиц в разрядах маски?
(Ответ: 12)
"""
from ipaddress import ip_network
hostIP = "211.208.38.203"
netIP = "211.208.0.0"
for ones in range(1,32):
  net = ip_network( f"{hostIP}/{ones}", 0 )
  if str(net.network_address) == netIP:
    print( ones )
    break
