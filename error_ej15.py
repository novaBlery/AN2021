I0 = 0.09531017980432493
n = 1

while n <= 25:
    In = (1/n)-10*I0
    I0 = In
    print("I" + str(n) + " = " + str(In))
    n += 1


