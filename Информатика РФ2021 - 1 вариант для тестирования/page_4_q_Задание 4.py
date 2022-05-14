for s in range(100):
    k = s
    n = 600
    while n > k:
        k = k+3
        n = n-6
    if n == 210:
        print(s)
