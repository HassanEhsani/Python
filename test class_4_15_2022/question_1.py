from random import randint


n = randint(100000, 1000000)
print(n)
s6 = n % 10
s1 = n//100000
s5 = (n//10) % 10
s4 = (n//100) % 10
s3 = (n//1000) % 10
s2 = (n//10000) % 10
if ((s1+s2+s3) == (s4+s5+s6)):
    print("good")
else:
    print("not good")
