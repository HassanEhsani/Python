N = 5
A = [0]*N
print("please enter array")
A = [int(input()) for i in range(N)]
S = 0
for i in range(N):
    S = S+A[i]
print("the average= ", S/N)
