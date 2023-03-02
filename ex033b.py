n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite outro número: '))
maior = n1
if n1 < n2 > n3:
    maior = n2
if n1 < n3 > n2:
    maior = n3
menor = n1
if n1 > n2 < n3:
    menor = n2
if n1 > n3 < n2:
    menor = n3
print('O maior número digitado foi {} e o menor foi {}'.format(maior, menor))
