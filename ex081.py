lista = list()
while True:
    lista.append(int(input('Digite um número: ')))
    resposta = str(input('Quer continuar? [S/N] '))
    if resposta in 'nN':
        break
print('-='*40)
print(f'Você digitou {len(lista)} elementos')
lista.sort(reverse=True)
print(f'Os valores digitados em ordem decrescente são: {lista}')
if 5 not in lista:
    print('O valore 5 não faz parte da lista')
else:
    print(f'O valore 5 faz parte da lista e está na posição {lista.index(5)+1}')
