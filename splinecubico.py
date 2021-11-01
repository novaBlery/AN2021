def splineCub(h, a, ai, c, ci):
    B = (1/h) * (a-ai) - (h/3) * (c+(2*ci))
    print("b =" + str(B))
    D = (1/(3*h)) * (c-ci)
    print("d =" + str(D))

splineCub(1,3,4.1, 0, -0.4702)