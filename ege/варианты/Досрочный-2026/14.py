def f(n):
    a = []
    while n:
        a = [n%27] + a
        n//=27
    k = 0
    for cif in a:
        if cif%2 == 0 and cif > 9:
            k += 1
    return k
print(f(2*2187**567+729**566-2*243**565+81**564-2*27**563-6561))