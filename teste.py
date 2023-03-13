from random import randint
lista = dict()
for c in range(0, 4):
    lista[f'Jogador{c+1}'] = int(randint(0, 6))
for k, v in lista.items():
    print(f'{k} tirou {v}')
print('RANKING DOS JOGADORES')
