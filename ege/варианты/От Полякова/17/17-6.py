k = 0
kv = 2**0.5
for x in range(0, 300):
    for y in range(-300, 1):
        if x > 0 and x < 203 and y > -203 and y < 0 or x < 203 + 20*kv and x > 203 + 20*kv - 20 and y < -203 + 20*kv and y > -203 + 20*kv - 20:
            k += 1
print(k)