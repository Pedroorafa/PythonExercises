dados = dict()

dados['Nome'] = str(input('Digite o nome do aluno(a): '))
dados['Média'] = float(input(f'Digite a média de {dados["Nome"]}: '))

if dados['Média'] >= 70:
    dados['Situação'] = 'Aprovado'
elif 5 <= dados['Média'] < 70:
    dados['Situação'] = 'Recuperação'
else:
    dados['Situação'] = 'Reprovado'
for k, v in dados.items():
    print(f'{k} é igual a {v}')
