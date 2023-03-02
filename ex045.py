#jokenpô
from random import randint
itens = ('PEDRA', 'PAPEL', 'TESOURA')
pc = randint(1, 3)
print('-=' * 20)
print('JOKENPÔ')
print('-=' * 20)
print('[ 0 ] PEDRA')
print('[ 1 ] PAPEL')
print('[ 2 ] TESOURA')
j = int(input('Qual a sua escolha? '))
print('-=' * 12)
print('Você jogou {}'.format(itens[j]))
print('Computador jogou {}'.format(itens[pc]))
print('-=' * 12)
if pc == 0:
    if j == 0:
        print('Impate')
    elif j == 1:
        print('PAPEL embrulha PEDRA, você ganhou!!!')
    elif j == 2:
        print('PEDRA esmaga TESOURA, você perdeu!!!')
if pc == 1:
    if j == 1:
        print('Impate')
    if j == 0:
        print('PAPEL embrulha PEDRA, você perdeu!!!')
    if j == 2:
        print('TESOURA corta PAPEL, você ganhou!!!')
if pc == 2:
    if j == 2:
        print('Impate')
    if j == 0:
        print('PEDRA esmaga TESOURA, você ganhou!!!')
    if j == 1:
        print('TESOURA corta PAPEL, você perdeu!!!')
print('-='*20)
