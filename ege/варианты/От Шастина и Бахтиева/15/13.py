from ipaddress import *
a = ip_network("250.128.212.1/255.255.224.0", 0)
print(a[0])
print(bin(250)[2:])
print(bin(128)[2:])
print(bin(192)[2:])
print(bin(224)[2:])