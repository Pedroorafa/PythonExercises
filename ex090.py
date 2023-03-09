dados = dict()

dados['Nome'] = str(input('Digite o nome do aluno(a): '))
dados['Média'] = int(input('Digite a média do aluno(a): '))

if dados['Média'] >= 70:
    print('O aluno(a) está aprovado(a)')
else:
    print('O aluno(a) está reprovado(a)')
