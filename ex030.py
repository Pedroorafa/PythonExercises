#crie um programa que leia um numero inteiro e mostre se é par ou impar
n = int(input('Digite um número: '))
if n % 2 == 0:
    print('O número digitado foi {} e ele é par'.format(n))
else:
    print('O número digitado foi {} e ele é ímpar'.format(n))
