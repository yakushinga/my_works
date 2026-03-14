from ipaddress import *
a = ip_network("218.194.82.148/255.255.255.192", 0)
print(a[-2])