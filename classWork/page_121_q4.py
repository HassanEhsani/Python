from random import randint


N = 10
A = [0]*N
for i in range(N):
    A[i] = randint(0,5)
print("Array: ",A)
x=int(input("enter the number if you want: "))
i = c = 0
while (i<N):
    if A[i]==x:
        print('A[',i,']=',A[i])
        c +=1
    i +=1
if c ==0:
    print("not found!")