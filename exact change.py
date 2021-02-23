from typing import Type
dollars = int()
penny = int()
cost_change = int(input())
if cost_change <= 0:
    print('no change')

else:
     dollars = cost_change//100
     cost_change%= 100

     quarters = (cost_change // 25)
     cost_change%= 25

     dimes = cost_change // 10
     cost_change%= 10

     nickel = cost_change // 5
     cost_change%= 5
     pennies = cost_change
     if dollars > 1:
        print('%d dollars' % dollars)
     elif dollars == 1:
        print('%d dollar'%dollars)

     if quarters > 1:
        print('%d quarters'%quarters)
     elif quarters == 1:
        print('%d quarter'%quarters)

     if dimes > 1:
        print('%d dimes'%dimes)
     elif dimes == 1:
        print('%d dime'%dimes)

     if nickel > 1:
        print('%d nickels'%nickel)
     elif nickel == 1:
        print('%d nickel'%nickel)

     if pennies > 1:
            print('%d penny'%penny )
     elif pennies == 1:
            print('1 penny')
