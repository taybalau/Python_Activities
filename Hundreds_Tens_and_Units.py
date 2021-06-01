# While-true loop and if-elif-else structure exercise: a program which asks the user to enter an integer,
# positive and less than 1000 and then indicates its hundred, tens and units

num = input('Enter an integer, positive and less than 1000: ')
num1 = None

while True:
    try:
        num1 = int(num)
    except:
        print('Please enter a numeric value!')
        num = input('Enter an integer, positive and less than 1000: ')
        continue

    if num1 > 1000:
        print('Please enter a number less than 1000!')
        num = input('Enter an integer, positive and less than 1000: ')
        continue

    if num1 < 0:
        print('Please enter a positive number')
        num = input('Enter an integer, positive and less than 1000: ')
        continue
    break

if 10 > num1 >= 0:
    print(f'{num1} unit(S)')
elif num1 == 10:
    num2 = num1 / 10
    print(f'{num2} ten(s) and 0 unit(s)')
elif num1 == 100:
    num2 = num1 / 100
    print(f'{num2} hundred(s), 0 ten(s) and 0 unit(s)')
elif num1 == 1000:
    num2 = num1 / 100
    print(f'{num2} hundred(s), 0 ten(s) and 0 unit(s)')
elif 100 > num1 > 10:
    dez1 = ((num1 % 10) - num1) / 10
    uni1 = num1 % 10
    if dez1 < 0:
        dez2 = (-1) * dez1
        print(f'{dez2} ten(s) and {uni1} unit(s)')
        quit()
    print(f'{dez1} ten(s) and {uni1} unidade(s)')
elif 1000 > num1 > 100:
    cen1 = ((num1 % 100) - num1) / 100
    dez1 = (num1 % 100) - (num1 % 10)
    uni1 = num1 % 10
    if cen1 < 0:
        cen2 = (-1) * cen1
        print(f'{cen2} hundred(s), {dez1} ten(s) and {uni1} unit(s)')
        quit()
    print(f'{cen1} hundred(s), {dez1} ten(s) and {uni1} unit(s)')
