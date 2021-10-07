import math

print("{:<40} {:<40} {:<40} {:<40} {:<20} {:<10}".format('VALOR DE i','VALOR DE h','VALOR REAL','VALOR APROX','TRUNCADO','REDONDEADO')) #Formato tabla
for n in range(1,31):
    e = math.e
    x = 0
    h = 2**(-n)
    func = (e**(x + h) - e**(x)) / h
    real = e**x
    trunc = math.trunc(func)
    redon = round(func)
    print("\n" + "\033[1;37m" + "{:<40} {:<40} {:<40} {:<40} {:<20} {:<10}".format(n, h, real, func, trunc, redon))
