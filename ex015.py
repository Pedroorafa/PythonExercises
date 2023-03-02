d = int(input('Por quantos dias irá alugar o carro? '))
km = float(input('Quantos km pretende rodar? '))
t = d * 60 + km * 0.15
print('O total a paragar pelo aluguel do carro é {:.2f} reais'.format(t))
