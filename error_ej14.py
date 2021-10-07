import math

print("{:<40} {:<40} {:<40} {:<40} {:<20} {:<10}".format('VALOR DE i','VALOR DE h','VALOR REAL','VALOR APROX','E. ABSOLUTO','E. REAL')) #Formato tabla
for n in range(1,31):
    e = math.e
    x = 0
    h = 2**(-n)
    func = (e**(x + h) - e**(x - h)) / 2 * h
    real = e**x
    eabs = abs(func - real)
    ereal = eabs / abs(real)
    print("\n" + "\033[1;37m" + "{:<40} {:<40} {:<40} {:<40} {:<20} {:<10}".format(n, h, real, func, eabs, ereal))