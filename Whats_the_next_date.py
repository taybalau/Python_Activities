# if-else-elif exercise: A program that asks the user for the day,
# month and year and determines the next date.

dd = input('Enter a day: ')
mm = input('Enter a month: ')
yyyy = input('Enter a year: ')

try:
    dd1 = int(dd)
    mm1 = int(mm)
    yyyy1 = int(yyyy)
except:
    print('Enter only integers')
    quit()

dd2 = dd1 + 1

if dd1 <= 0 or dd1 > 31:
    print('Invalid date')
    quit()
elif mm1 <= 0 or mm1 > 12:
    print('Invalid date')
    quit()
elif yyyy1 <= 0:
    print('Invalid date')
    quit()

if mm1 == 2:
    if yyyy1 % 4 == 0 and yyyy1 % 100 != 0 or yyyy1 % 400 == 0:
        if dd1 > 29:
            print('Invalid date')
            quit()
        elif dd1 == 29:
            print(f'The next date is: 1 / {mm1 + 1} / {yyyy1}')
        else:
            print(f'The next date is: {dd2} / {mm1} / {yyyy1}')
    elif dd1 > 28:
        print('Invalid date')
        quit()
    else:
        print(f'The next date is: {dd2} / {mm1} / {yyyy1}')

if dd1 == 31:
    if mm1 in (4, 6, 9, 11):
        print('Invalid date')
        quit()

if dd1 == 31:
    if mm1 in (1, 3, 5, 7, 8, 10):
        print(f'The next date is: 1 / {mm1 + 1} / {yyyy1}')
        quit()
elif dd1 == 30:
    if mm1 in (4, 6, 9, 11):
        print(f'The next date is: 1 / {mm1 + 1} / {yyyy1}')
        quit()

if dd2 == 32 and mm1 == 12:
    print(f'The next date is: 1 / 1 /  {yyyy1 + 1}')
elif mm1 in (1, 3, 5, 7, 8, 10, 12):
    print(f'The next date is: {dd2} / {mm1} / {yyyy1}')
elif mm1 in (4, 6, 9, 11):
    print(f'The next date is: {dd2} / {mm1} / {yyyy1}')
