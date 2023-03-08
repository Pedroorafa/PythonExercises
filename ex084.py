pessoas = list()
dados = list()
pmaior = list()
nmaior = list()
nmenor = list()
pmenor = list()
while True:
    dados.append(str(input('Digite o nome: ')))
    dados.append(int(input('Digite o peso: ')))
    r = str(input('Deseja continuar? [S/N] '))
    pessoas.append(dados[:])
    dados.clear()
    if r in 'Nn':
        break
for p in pessoas:
    if p[1] >= 100:
        pmaior.append(p[1])
        nmaior.append(p[0])
    elif p[1] <= 70:
        pmenor.append(p[1])
        nmenor.append(p[0])
print('-='*40)
print(f'Você cadastrou {len(pessoas)} pessoas')
print(f'Os maiores pesos foram {pmaior} de {nmaior}')
print(f'Os menores pesos foram {pmenor} de {nmenor}')
