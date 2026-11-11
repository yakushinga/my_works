from ipaddress import *
a = ip_network("135.13.142.29/255.255.255.128", 0)
print(a[-2])