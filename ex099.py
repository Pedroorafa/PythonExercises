from time import sleep
def maior(* num):
    cont = maior = 0
    print('-='*30)
    print('Analizando os valores passados... ')
    for valor in num:
        sleep(0.5)
        print(f'{valor} ', end='')
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valores')
    print(f'O maior valor informado foi {maior}')


maior(4, 79, 54, 2, 0)
maior(6, 890, 10002, 3, 5, 3, 15)
