# numbers are entered from the keyboard, the input ends with the number 0. Determine the minimum of the entered Fibonacci numbers. Output "none" if there are no Fibonacci numbers in the sequence.
# Fibonacci numbers are a sequence of numbers that starts with two ones and each next number is equal to the sum of the previous two: 1, 1, 2, 3, 5, 8, 13,
f = [0]*12
f[0] = f[1] = 1
for i in range(2, 12):
    f[i] = f[i-1]+f[i-2]
print(f)
x = int(input())

count = 0
while x != 0:
    if x in f:
        count += 1
        if count == 1:
            Min = x
        else:
            if x < Min:
                Min = x
    x = int(input())
if count == 0:
    print("not")
else:
    print(Min)
