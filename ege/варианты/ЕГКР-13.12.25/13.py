from ipaddress import *
a = ip_network("190.202.83.62/255.255.252.0", 0)
print(a[-2], 190+202+83+254)