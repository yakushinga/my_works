minn = 10**20
for x in range(16, 21):
    for y in range(21):
        n = x**4 + 3*x**3 + 15*x**2 + x + y + 21**4 + 5*21**3 + x*21**2 + 5*21 + y
        if n % 32 == 0 and n < minn:
            minn = n
print(minn//32)
