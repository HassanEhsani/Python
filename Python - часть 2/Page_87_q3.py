from random import randint
A = [0]*10
B = [0]*10
for i in range(10):
    A[i]= randint(0,99)
    B[i]=A[i]%10
print(A)
print(B)