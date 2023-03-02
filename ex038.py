#leia dois número inteiros e compareos
#mostre menssagem: o primeiro valor é maior; o segundo valor é maior'não existe valor maior, os dois são iguais
n1 = int(input('Escreva um número: '))
n2 = int(input('Escreva outro número: '))
if n1>n2:
    print('O primeiro valor é maior')
elif n2>n1:
    print('O segundo valor é maior')
else:
    print('Os valores são iguais')
