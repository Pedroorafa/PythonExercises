#leia nome idade e sexo de 4 pessoas
#mostre a média de idade, qual o nome do homem mais velho e quantas mulheres tem menos de 20 anos
maioridadehomem = 0
nomedovelho = ''
somaidade = 0
mulheresnovas = 0
for c in range(1, 5):
    print('{} PESSOA'.format(c))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [F/M]'))
    somaidade += idade
    if c == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomedovelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomedovelho = nome
    if sexo in 'Ff' and idade > 20:
        mulheresnovas += 1
media = somaidade / 4
print('A média de idade do grupo é {}, o homem mais velho se chama {} e tem {} anos'.format(media, nomedovelho, maioridadehomem))
print('Tem um total de {} mulheres a baixo dos 20 anos'.format(mulheresnovas))


