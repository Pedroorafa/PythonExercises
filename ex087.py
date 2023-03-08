lista = list()
par = soma = 0
for c in range(0, 9):
    n = int(input('Digite um número: '))
    lista.append(n)
    if n %2 == 0:
        par += n
soma = lista[2] + lista[5] + lista[8]
print('-='*20)
print(f'[ {lista[0]} ][ {lista[1]} ][ {lista[2]} ]')
print(f'[ {lista[3]} ][ {lista[4]} ][ {lista[5]} ]')
print(f'[ {lista[6]} ][ {lista[7]} ][ {lista[8]} ]')
print('-='*20)
print(f'A soma dos valores pares é {par}')
print(f'A soma dos valores da terceira coluna é {soma}')
print(f'O maior valor da segunda linha é {max(lista[3:6])}')

