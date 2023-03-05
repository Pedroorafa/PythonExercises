lista = list()
resposta = ''
while True:
    valor = (int(input('Digite um valor: ')))
    if valor not in lista:
        lista.append(valor)
    else:
        print('Valor duplicado, porfavor digite outro número')
    resposta = str(input('Quer continuar? [S/N] '))
    if resposta in 'nN':
        break
print('-='*40)
print(f'Você digitou os valores {lista}')