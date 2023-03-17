def leiaint(msg):
    ok = False
    while True:
        l = str(input(msg))
        if l.isnumeric():
            l = int(l)
            ok = True
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
        if ok:
            break
    return l

n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {n}')