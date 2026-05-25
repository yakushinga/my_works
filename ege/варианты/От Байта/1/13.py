from ipaddress import *
a = ip_network("172.45.129.10/255.240.0.0", 0)
print(a[-2])