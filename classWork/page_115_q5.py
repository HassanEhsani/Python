print("please enter the number")
N = int(input())
A = [0]*N
A[0] = A[1] = 1
for i in range(2, N):
    A[i] = A[i-1]+A[i-2]
print("the number of fibonachi: ", A)
