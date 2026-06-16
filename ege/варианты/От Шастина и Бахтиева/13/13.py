from ipaddress import *
a = ip_network("167.111.222.0/255.255.128.0", 0)
print(a[0])
print(bin(167)[2:])
print(bin(111)[2:])
print(bin(128)[2:])
print(bin(0)[2:])

def fact(n):
    r = 1
    for i in range(2, n+1):
        r*=i
    return r

def soch(n, k):
    r = fact(n)//(fact(k)*fact(n-k))
    return r

r = 0
for k in range(0, 16):
    if (k + 12) % 7 != 0:
        r += soch(15, k)
print(r)