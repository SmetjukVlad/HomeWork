money = 1000
procent = float(input('Enter the deposit percentage: '))/100
month = 0

while True:
    money = money*(1+procent)
    month +=1
    if money >= 1100:
        print ('Number of months {0}. Account balance {1}'.format(month,round(money,2)))
        break

