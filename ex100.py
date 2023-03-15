from time import sleep
from random import randint
lista = list()
def sorteio(num):
    print(f'Sorteando valores da lista: ', end=' ')
    for c in range(0, 5):
        sleep(0.5)
        n = randint(0, 99)
        print(n, end=' ')
        num.append(n)
    print('FIM!')
def somaPAR(num):
    soma = 0
    for i, v in enumerate(num):
        if v % 2 == 0:
            soma += v
    print(f'\nSomando os valores pares de {num}, temos {soma}')

sorteio(lista)
somaPAR(lista)
