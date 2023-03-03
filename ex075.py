#leia 4 valores e guarde em uma tupla
#mostre quantas vezes apareceu o valor 9
#em que posição foi digitado o primeiro valor 3
#Quais foram os números pares
import math
num = (int(input('Digite um número: ')),
       int(input('Digite outro número: ')),
       int(input('Digite outro número: ')),
       int(input('Digite outro número: ')))
print(f'Os números digitados foram {num}')
print(f'o número 9 apareceu {num.count(9)} vezes na tupla')
if num.count(3) == 0:
    print('O valor 3 não foi encontrado na tupla')
else:
    print(f'O valor de 3 foi encontrado na posição {num.index(3)+1}')
print('Os números pares foram: ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')

