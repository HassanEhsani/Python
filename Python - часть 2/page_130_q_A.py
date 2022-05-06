def AveN(n):
    print("Введите", n, "чисел:")
    A = [0]*n
    sum = 0
    for i in range(n):
        A[i] = int(input())
        sum += A[i]
    return sum/n


n = int(input("Введите количество чисел: "))
sred = AveN(n)
print(sred)
