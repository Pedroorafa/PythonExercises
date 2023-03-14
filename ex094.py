dados = dict()
cadastro = list()
mulheres = list()
acima = list()
n = total = média = 0
while True:
    dados['Nome'] = str(input('Qual é o seu nome? '))
    dados['Sexo'] = str(input('Qual é o seu sexo? [M/F] '))
    dados['Idade'] = int(input('Qual a sua idade? '))
    continuar = str(input('Deseja continuar? [S/N] '))
    cadastro.append(dados.copy())
    total += dados['Idade']
    if dados['Sexo'] in 'fF':
        mulheres.append(dados['Nome'])
    n += 1
    if continuar in 'nN':
        break
média = total // n
print('-='*30)
print(cadastro)
print('-='*30)
print(f'-> O grupo tem {n} pessoas')
print(f'-> A média de idade foi {média}')
print(f'-> As mulheres cadastradas foram: {mulheres}')
for c in range(0, n):
    if cadastro[c]['Idade'] >= média:
        acima.append(cadastro[c])
print('-> Pessoas que estão com idade acima da média:')
for i in acima:
    print(f'\n Nome = {i["Nome"]}; Sexo = {i["Sexo"]}; Idade = {i["Idade"]}', end='')
print('<< ENCERRADO >>')
