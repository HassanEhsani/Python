# enter the number N and display all the powers of the number 2 from 21
N = int(input("Input N (2-10):"))
for i in range(1,N+1):
    print(i,"2^",i,"=",2**i,sep="")