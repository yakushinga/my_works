# **4*4736*1

for i in range(0, 100000):
    n = int(str(i//100) + "4" + str(i//10%10) + "4736" + str(i%10) + "1")
    if n%7993 == 0:
        print(n, n//7993)