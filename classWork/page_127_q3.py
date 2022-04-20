from random import randint

N = 10
A = [0]*N
for i in range(N):
    A[i]= randint(10,100)
print("array: ",A)
i = 0
Ma = Mi = 0
while (i<N):
    if A[i]>A[Ma]:
        Ma = i
    if A[i]<A[Mi]:
        Mi = i
    i +=1
print("Max. number is ",Ma, " = ",A[Ma])
print("Min. number is ",Mi, " = ",A[Mi])