# find all five-digit numbers that when divided by 133 have a remainder of 125 and when divided by 134, have a reminder of 111
for i in range(10000,100000):
    if i%133==125 and i%134==111:
        print(i)