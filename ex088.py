from random import randint
import time
lista = list()
n=0
print('-'*30)
print('JOGUE NA MEGA SENA')
print('-'*30)
j = int(input('Quantos jogos você quer que eu sorteie? '))
print('-='*3, f'SORTEANDO {j} JOGOS', '-='*3)
for c in range(0, j):
    time.sleep(1)
    print(f'Jogo {c+1} :',end='')
    for c in range(0,6):
        n = randint(1, 60)
        if n not in lista:
            lista.append(n)
    print(lista)
    lista.clear()
