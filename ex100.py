from time import sleep
from random import randint
lista = list()
def sorteio():
    print(f'Sorteando valores da lista: ', end=' ')
    for c in range(0, 5):
        sleep(0.5)
        n = randint(0, 99)
        print(n, end=' ')
        lista.append(n)
    print('FIM!')
def somaPAR():
    soma = 0
    for i, v in enumerate(lista):
        if v % 2 == 0:
            soma += v
    print(f'\nSomando os valores pares de {lista}, temos {soma}')

sorteio()
somaPAR()
