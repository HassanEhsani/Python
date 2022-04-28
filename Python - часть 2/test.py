from multiprocessing import Condition
from random import randint
n = int(input())
A = [0]*n
for i in range(n):
    A[i]=randint(1,100)
print(A," ")

k=0
s=0
for i in range(n):
    if Condition :
        k +=1
        s +=A[i]
    print(k,s)
