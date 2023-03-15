from time import sleep
def contador(a, b, c):
    if c == 0:
        c = 1
    if c < 0:
        c *= -1
    print('-=' * 20)
    print(f'Contagem de {a} até {b} de {c} em {c}')
    print('-=' * 20)
    while True:
        sleep(0.3)
        print(a, end=' ')
        if a < b:
            a += c
            if a >= b:
                print('FIM!')
                break
        elif a > b:
            a -= c
            if a <= b:
                print('FIM!')
                break


contador(1, 10, 1)
contador(10, 0, 2)
a = int(input('Início: '))
b = int(input('Fim: '))
c = int(input('Passo: '))
contador(a, b, c)
