#leia um número inteiro e diga se ele é ou não um número primo
#primo = /1 ou ele mesmo
n = int(input('Digite um número: '))
for c in range(2, n):
    s = n % c
    if s == 0:
        print('Esse número não é primo')
        exit()
print('Esse número é primo')
