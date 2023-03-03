#crie 5 números aleatórios e os coloque em uma tupla
#mostre a listagem dos números gerados
#e qual foi o menor e o maoir
from random import randint
n1 = randint(1, 100)
n2 = randint(1, 100)
n3 = randint(1, 100)
n4 = randint(1, 100)
n5 = randint(1, 100)
numeros = n1, n2, n3, n4, n5
maior = n1
menor = n1
print(numeros)
if n2 > maior:
    maior = n2
if n3 > maior:
    maior = n3
if n4 > maior:
    maior = n4
if n5 > maior:
    maior = n5
print(f'O maior número digitado foi {maior}')
if menor > n2:
    menor = n2
if menor > n3:
    menor = n3
if menor > n4:
    menor = n4
if menor > n5:
    menor = n5
print(f'O menor número digitado foi {menor}')
