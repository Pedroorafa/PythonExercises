#faça um programa que leia o sexo da pessoa
#só aceite F ou M, caso esteja errado peça para que digite novamente
sexo = str(input('Digite seu sexo [F/M]: ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Não foi possível registar, digite novamente o seu sexo [F/M]: '))
print('Seu sexo correspode a {}'.format(sexo))