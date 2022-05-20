from random import randrange


def f(a, b, c, d):
    f = (a or d) == ((b or b) <= c)
    if f:
        return 1
    else:
        return 0


print("a", "b", "c", "d", "|", "f")
for a in range(2):
    for b in range(2):
        for c in range(2):
            for d in range(2):
                print(a, b, c, d, "|", f(a, b, c, d))
