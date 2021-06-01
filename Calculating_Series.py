"""
For and range exercises: A program that asks for a 'n' number and calculates the following series
a) 1 + 2 + 3 + 4 ... + n
b) 1 - 2 + 3 - 4 + 5 ... + (2n - 1)
c) 1 + 3 + 5 + 7 ... ... + (2n - 1)
"""

# a
n = int(input(''))
soma = 0

for num in range(n+1):
    soma = soma + num
print(soma)

# b
n = int(input(''))
soma = 0

for num in range(2*n):
    if num % 2 != 0:
        soma = soma + num
    else:
        soma = soma - num
print(soma)

# c
n = int(input(''))
soma = 0

for num in range(2*n):
    if num % 2 != 0:
        soma = soma + num
    else:
        continue
print(soma)
