#leia o peso de 5 pessoas e fale qual foi o maior e o menor peso
for c in range(1, 5):
    peso = float(input('Qual é o seu peso em kg? '))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso
    print('O maior peso foi {} kg e o menor foi {} kg'.format(maior, menor))
