def Nuli(n):
    o = 0
    while n > 0:
        if n % 2 == 0:
            o += 1
        n = n//2
    return o


i = int(input("Введите количество чисел: "))
print("В число", i, "цифр ноль", Nuli(i), "штук")
