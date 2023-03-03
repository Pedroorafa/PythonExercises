#leia 4 valores e guarde em uma tupla
#mostre quantas vezes apareceu o valor 9
#em que posição foi digitado o primeiro valor 3
#Quais foram os números pares
import math
n1 = int(input('Escreva um número: '))
n2 = int(input('Escreva outro número: '))
n3 = int(input('Escreva outro número: '))
n4 = int(input('Escreva outro número: '))
num = n1, n2, n3, n4
print(num)
print(f'o número 9 apareceu {num.count(9)} vezes na tupla')
if num.count(3) == 0:
    print('O valor 3 não foi encontrado na tupla')
else:
    print(f'O valor de 3 foi encontrado na posição {num.index(3)}')
print('Os números pares foram: ')
if n1 % 2 == 0:
    print(n1, end=', ')
if n2 % 2 == 0:
    print(n2, end=', ')
if n3 % 2 == 0:
    print(n3, end=', ')
if n4 % 2 == 0:
    print(n4, end='')
