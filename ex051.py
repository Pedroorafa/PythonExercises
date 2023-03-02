#leia o primeiro termo e a razão de uma progessão aritimética
#e mostre os 10 primeiros termos dessa progressão
p = int(input('Digite em que número irá começar: '))
r = int(input('Digite a progressão que irá ser feira: '))
d = p + (10 -1) * r
for c in range (p, d, r):
    print(c)
