total = total1k = contagem = maisbarato =0
nomebarato = ''
while True:
    nome = str(input('Qual o nome do produto? '))
    preço = float(input('Qual o preço desse produto? '))
    contagem += 1
    total += preço
    if preço >= 1000:
        total1k += 1
    if contagem == 1 or preço < maisbarato:
        maisbarato = preço
        nomebarato = nome
    opção = ' '
    while opção not in 'SN':
        opção = str(input('Deseja continuar?[s/n] ')).strip().upper()[0]
    if opção == 'N':
        break
print(f'O total gasto foi {total}, sendo que {total1k} custaram mais de R$1000 e o mais barato foi {nomebarato}')
