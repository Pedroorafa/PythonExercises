#desafio 9 só que usando for
n = int(input('Digite um número: '))
x = 1
for c in range(1, 11):
    print('{} x {} = {}'.format(n, x, n * x))
    x = x+1