from random import randint
lista = dict()
listagem = list()
for c in range(0, 4):
    lista['Nome'] = str(f'Jogador {c+1}')
    lista['Dados'] = int(randint(0, 6))
    listagem.append(lista.copy())
print('Valores Sorteados:')
for c in range(0, 4):
    print(f'O {listagem[c]["Nome"]} tirou {listagem[c]["Dados"]}')
print('Ranking dos jogadores')
