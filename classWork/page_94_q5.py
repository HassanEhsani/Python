for i in range(100,1000):
    n1=i//100
    n2=(i//10)%10
    n3=i%10
    if i==n1 **3+n2**3+n3**3:
        print(i)