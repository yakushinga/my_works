from ipaddress import *
a = ip_network("98.112.180.225/255.255.240.0", 0)
print(a[-2])