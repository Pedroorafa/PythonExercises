#escreva um programa que leia a velocidade de um carro
#se ele ultrapassar 80km/h, mostre uma menssagem que ele foi multado
#a multa vai custar R$ 7.00 por cada km acima do limite
v = int(input('Digite (apenas números) a velocidade que você está dirigindo: '))
if v > 80:
    print('Você acaba de receber uma multa no valor de R${:.2f}'.format((v - 80)*7))
else:
    print('Parabéns! Voce esta dentro da lei!')
