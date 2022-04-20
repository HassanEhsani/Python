# A prime number is a number that is only divisible by itself and 1. Enter a natural number N and print all prime numbers in the range from 2 to N.
N = int(input("find the number: "))
isPrime = True
for i in range(2, round(N**0.5)+1):
    if N % i == 0:
        isPrime = False
print("your number is= ", isPrime)
