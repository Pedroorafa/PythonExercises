#crie um programa que leia 2 valores e mostre um menu
# 1 somar 2 multiplicar 3 maior 4 novos numero(trocar numeros) 5 sair do programa
#o programa deverá realizar a ação solicitada em cada um dos caso
c = 0
n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
while c != 5:
    print('''    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Mostrar maior
    [ 4 ] Escrever novos números
    [ 5 ] Para sair''')
    c = int(input('Escolha a opção: '))
    if c == 1:
        print(n1 + n2)
    elif c == 2:
        print(n1 * n2)
    elif c == 3:
        if n1 > n2:
            print(n1)
        else:
            print(n2)
    if c == 5:
        print('Programa finalizado')
        exit()
    if c == 4:
        print('Reset')
        n1 = float(input('Digite um número: '))
        n2 = float(input('Digite outro número: '))

