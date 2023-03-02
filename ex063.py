#escreva um programa q leia um numero n inteiro
#e mostre na tela os n primeiros elementos de uma sequancia de numeros de fibonacci
print('='*13)
print('Sequência de Fibonacci')
print('='*13)
seq = int(input('Quantas sequências você quer mostrar? '))
print('-~-'*10)
n1 = 0
n2 = 1
n3 = 0
print('{} → {}'. format(n1, n2), end='')
c = 3
while c <= seq:
    n3 = n1 + n2
    print(' → {}'.format(n3), end= '')
    n1 = n2
    n2 = n3
    c += 1
print(' → FIM')
