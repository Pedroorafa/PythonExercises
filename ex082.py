lista = list()
par = list()
imp = list()
while True:
    lista.append(int(input('Digite um número: ')))
    resposta = str(input('Deseja continuar? [S/N] '))
    if resposta in 'nN':
        break
for n in lista:
    if n % 2 == 0:
        par.append(n)
    else:
        imp.append(n)
print(f'Os números digitados foram {lista}')
print(f'Os números pares digitados foram {par}')
print(f'OS números ímpares digitados foram {imp}')
