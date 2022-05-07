numbers = [2,2,3,1,2,5,4]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)