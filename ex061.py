#refaça o ex051, mostrando os primeiros termos da razão usando while
p = int(input('Digite em que número irá começar: '))
r = int(input('Digite a progressão que irá ser feira: '))
t = p
c = 1
while c <= 10:
    print('{} >'.format(t), end='')
    t += r
    c += 1
print('FIM')
