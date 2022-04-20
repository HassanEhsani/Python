# A natural number is called an Armstrong number if the sum of the digits of the number raised to the Nth power (where N is the number of Digits in the number) is equal to the number itself for example 153=13+53+33 find all three digit armstrong numbers
for i in range (100,1000):
    c1=i%10
    c2 = i//10%10
    c3=i//100
    if i ==c1**3+c2**3+c3**3:
        print(i)