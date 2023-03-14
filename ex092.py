from datetime import date
while True:
    cadastro = dict()
    cadastro['Nome'] = str(input('Digite seu nome: '))
    cadastro['Idade'] = (date.today().year - int(input('Digite sua data de nascimento: ')))
    cadastro['CTPS'] = int(input('Digite o número da sua carteira de trabalho: [0 se não tem] '))
    if cadastro['CTPS'] == 0:
        break
    cadastro['Contratação'] = int(input('Digite o ano da sua contratação: '))
    cadastro['Salario'] = int(input('Digite o seu salário: '))
    cadastro['Aposentadoria'] = cadastro['Idade'] + ((cadastro['Contratação'] + 35) - date.today().year)
    break
print('-*'*10)
for k, v in cadastro.items():
    print(f'{k} tem o valor {v}')
print('-*'*10)
