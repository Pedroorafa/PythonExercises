c = maioridade = homens = menoridademulher = 0
print('-'*20)
print('CADASTRE UMA PESSOA')
print('-'*20)
while True:
    i = int(input('Idade: '))
    s = ' '
    while s not in 'FM':
        s = str(input('Sexo: [F/M] ')).strip().upper()[0]
    if i >= 18:
        maioridade += 1
    if s == 'M':
        homens += 1
    if s == 'F' and i < 20:
        menoridademulher += 1
    r = ' '
    while r not in 'SN':
        r = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    c += 1
    if r == 'N':
        break
print(f'Foram cadastrados {c} pessoas, {maioridade} tem mais de 18 anos, {homens} são homens e {menoridademulher} são mulheres com menos de 20 anos')