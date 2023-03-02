#leia de 0 a 9999 e mostre cada um dos digitos separados
#unidade
#dezena
#centena
#milhar
n = int(input('Digite um número: '))
ns = str(n)
if n<10000:
    if n>999:
        print('Unidade: {}\n'.format(ns[3]), 'Dezena: {}\n'.format(ns[2]), 'Centena: {}\n'.format(ns[1]), 'Milhar: {}'.format(ns[0]))
    if 1000>n>99:
        print('Unidade: {}\n'.format(ns[2]), 'Dezena: {}\n'.format(ns[1]), 'Centena: {}\n'.format(ns[0]))
    if 100>n>9:
        print('Unidade: {}\n'.format(ns[1]), 'Dezena: {}\n'.format(ns[0]))
    if 10>n>0:
        print('Unidade: {}\n'.format(ns[0]))
if n>9999:
    print('Número maior que o suportado')





