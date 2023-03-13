from random import randint
from time import sleep
lista = dict()
for c in range(0, 4):
    lista[f'Jogador{c+1}'] = int(randint(0, 6))
print('VALORES SORTEADOS: ')
for k, v in lista.items():
    sleep(1)
    print(f'{k} tirou {v}')
print('RANKING DOS JOGADORES: ')
lista_ordem = sorted(lista.items(), key=lambda x: x[1], reverse=True)
l = 0
for k, v in lista_ordem:
    sleep(1)
    print(f'{l+1}° Lugar {k} com {v}')
    l += 1
