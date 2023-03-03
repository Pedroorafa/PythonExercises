#crie uma única tupla com nome dos produtos e seus respectivos preços na sequência
#mostre uma listagem de preços organizando os dados de forma tabular
produtos = ('cafe',20,
            'coca', 8,
            'miojo', 2,
            'maionese', 18)
print('-'*40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-'*40)
for pos in range(0, len(produtos)):
    if pos % 2 == 0:
        print(f'{produtos[pos]:.<30}', end='')
    else:
        print(f'R${produtos[pos]:>5.2f}')
print('-'*40)