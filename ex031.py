#pergunte a distancia de uma viagem em km
#calcule o preço da passagem do onibus, cobrando R$0.50 por km para até 200km e R$0.45 para mais longas
d = float(input('Qual a dintância (apenas números) da sua viagem? '))
if d > 200:
    print('A sua passagem vai custar R${}'.format(d * 0.45))
else:
    print('A sua passagem vai custar R${}'.format(d * 0.50))
