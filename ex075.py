#leia 4 valores e guarde em uma tupla
#mostre quantas vezes apareceu o valor 9
#em que posição foi digitado o primeiro valor 3
#Quais foram os números pares
import math
n1 = int(input('Escreva um número: '))
n2 = int(input('Escreva outro número: '))
n3 = int(input('Escreva outro número: '))
n4 = int(input('Escreva outro número: '))
numeros = n1, n2, n3, n4
print(numeros)
print(f'o número 9 apareceu {numeros.count(9)} vezes na tupla')
print(f'O valor 3 foi encontrado na tupla na posição {numeros.index(3)}')
    ###falta terminar!!!!
