"""
List and while/for loop exercise:
A program that asks for multiple numbers as input and as output says:
a) the sum
b) the quantity
c) the average
d) the largest and the smallest number
e) the average of the even numbers
"""

lista = []
print('Insert an integer: ')
num = input()

while num != 'done':
    try:
        num1 = int(num)
        print('Insert an integer: ')
        num = input()
    except:
        print('Invalid value')
        print('Insert an integer: ')
        num = input()
    lista.append(num1)

soma = sum(lista)
print(f'The sum is {soma}')

tamanho = len(lista)
print(f'The amount of numbers informed was {tamanho}')

media = soma/tamanho
print(f'The average is {media}')

maior = max(lista)
print(f'The highest number is {maior}')

menor = min(lista)
print(f'The smallest number is {menor}')

lista2 = []

for num in lista:
    if num % 2 == 0:
        lista2.append(num)

media_pares = sum(lista2)/len(lista2)
print(f'The average of the even numbers is {media_pares}')
