dados = dict()
listagols = list()
lista = list()
partidas = gols = total = 0
while True:
    nome = str(input('Qual o nome do jogador: '))
    partidas = int(input('Quantas patidas ele jogou? '))
    for c in range(0, partidas):
        gols = int(input(f'Quantos gols ele fez na partida {c+1}? '))
        total += gols
        listagols.append(gols)
    dados['Nome'] = nome
    dados['Gols'] = listagols.copy()
    dados['Total'] = total
    lista.append(dados.copy())
    continuar = str(input('Deseja continuar? [S/N] '))
    print('-'*20)
    if continuar in 'nN':
        break
print('-='*30)
print(f'{"cod":<4}{"NOME":<10}{"Gols":<25}{"Total":>30}')
print('-'*20)
for i, l in enumerate(lista):
    print(f'{i:<4}{l["Nome"]:<10}{str(l["Gols"]):<25}{l["Total"]:>30}')
print('-'*20)
while True:
    op = int(input('Mostrar dados de quel jogador? [Digite 999 para encerrar] '))
    if op == 999:
        break
    if op <= len(lista)-1:
        print(f'-- LEVANTAMENTO DO JOGADOR {lista[op]["Nome"]}:')
        for p, l in enumerate(lista[op]["Gols"]):
            print(f'No jogo {p+1} ele(a) fez {l}')
        print('-'*20)
print('<<ENCERRADO>>')
