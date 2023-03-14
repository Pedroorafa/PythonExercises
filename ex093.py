dados = dict()
lista = list()
partidas = goals = total = 0
dados['Nome'] = str(input('Qual o nome do jogaodor: '))
partidas = int(input('Quantas patidas ele jogou? '))
for c in range(0, partidas):
    goals = int(input(f'Quantos gols ele fez na partida {c+1}? '))
    total += goals
    lista.append(goals)
dados['Goals'] = lista.copy()
dados['Total'] = total
print('-='*20)
print(dados)
print('-='*20)
for i, v in dados.items():
    print(f'O campo {i} tem o valor {v}')
print('-='*20)
print(f'O Jogador {dados["Nome"]} jogou {partidas} partidas')
for p, g in enumerate(lista):
    print(f'=> Na partida {p+1} fez {g} goals')
print(f'Foi um total de {total} gols')
