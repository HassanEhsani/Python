def Quant(n):
    q = 0
    while n > 0:
        n = n//10
        q += 1
    return q


i = int(input("Введите количество чисел:"))
print("В число", i, "цифр", Quant(i), "штук")
