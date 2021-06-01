# Decisão8_8

dd = input("Insira um dia: ")
mm = input("Insira um mês: ")
aaaa = input("Insira um ano: ")

try:
    dd1 = int(dd)
    mm1 = int(mm)
    aaaa1 = int(aaaa)
except:
    print("Insira apenas números inteiros")
    quit()

dd2 = dd1 + 1

if dd1 <= 0 or dd1 > 31:
    print("Data inválida")
    quit()
elif mm1 <= 0 or mm1 > 12:
    print("Data inválida")
    quit()
elif aaaa1 <= 0:
    print("Data inválida")
    quit()

if aaaa1 % 4 == 0 and aaaa1 % 100 != 0 or aaaa1 % 400 == 0:
    if mm1 == 2:
        if dd1 > 29:
            print("Data inválida")
            quit()
if mm1 == 2:
    if dd1 > 28:
        print("Data inválida")
        quit()
elif dd1 > 30:
    if mm1 == 4 or mm1 == 6 or mm1 == 9 or mm1 == 11:
        print("Data inválida")
        quit()

if dd2 == 32:
    if mm1 == 1 or mm1 == 3 or mm1 == 5 or mm1 == 7 or mm1 == 8 or mm1 == 10:
        print("A data seguinte é: 1 /", mm1 + 1, "/", aaaa1)
        quit()

if dd2 == 31:
    if mm1 == 4 or mm1 == 6 or mm1 == 9 or mm1 == 11:
        print("A data seguinte é: 1 /", mm1 + 1, "/", aaaa1)
        quit()

if mm1 == 2:
    if aaaa1 % 4 == 0 and aaaa1 % 100 != 0 or aaaa1 % 400 == 0:
        if dd2 == 30:
            print("A data seguinte é: 1 /", mm1 + 1, "/", aaaa1)
        else:
            print("A data seguinte é: ", dd2, "/", mm1, "/", aaaa1)
    else:
        print("A data seguinte é: ", dd2, "/", mm1, "/", aaaa1)
elif dd2 == 32 and mm1 == 12:
    print("A data seguinte é: 1 / 1 / ", aaaa1 + 1)
elif mm1 == 1 or mm1 == 3 or mm1 == 5 or mm1 == 7 or mm1 == 8 or mm1 == 10 or mm1 == 12:
    print("A data seguinte é: ", dd2, "/", mm1, "/", aaaa1)
elif mm1 == 4 or mm1 == 6 or mm1 == 9 or mm1 == 11:
    print("A data seguinte é: ", dd2, "/", mm1, "/", aaaa1)