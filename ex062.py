#melhore o ex061 perguntando se quer ver mais algum termos, o programa só para quando digitar 0
primeiro = int(input('Digite em que número irá começar: '))
razao = int(input('Digite a progressão que irá ser feira: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} >'.format(termo), end='')
        termo += razao
        cont += 1
    print('FIM')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados'.format(total))

