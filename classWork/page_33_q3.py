print('The cost of a pie: ', end='')

rub, cop = map(int, input().split())

count = int(input('Number of pies: '))

cop += rub*100

cop *= count

rub = cop // 100

cop = cop % 100

print('payment ', rub, ' руб. ', cop, ' коп.')
