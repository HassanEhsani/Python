def f(n):
    if n > 0:
        G(n-1)


def G(n):
    print("*",end="")
    if n > 1:
        print("*", end="")
        f(n-2)


f(13)
