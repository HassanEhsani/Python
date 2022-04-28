# the number N is entered from the keyboard, and then - N integers. Determine how many positive and how many negative numbers were entered (do not count zeros!).
n = int(input("enter the number(N): "))
k = m = 0
for i in range(n):
    
    x = int(input())
    if x > 0:
        k += 1
    elif x < 0:
        m += 1
print("The number of Positive=> ", k)
print("The number of Negative=> ", m)
