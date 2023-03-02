#calcule o valor do produto conforme a forma de pagamento
#a vista dinheiro ou cheque 10% de desconto
#a  vista no cartão 5% de desconto
#em até 2 vezes no cartão preço normal
#3x ou mais no cartão 20% de  juros no valor total
preco = float(input('Qual o valor do produto? '))
print('[ 1 ] À vista no dinheiro ou cheque')
print('[ 2 ] À no cartão')
print('[ 3 ] 2x no cartão')
print('[ 4 ] 3x ou mais no cartão')
print('[ 5 ] Finalizar')
opc = int(input('Qual a sua escolha? '))
if opc == 1:
    print('O valor a ser pago será R$ {:.2f}'.format(preco - (preco /10)))
elif opc == 2:
    print('O valor a ser pago será R$ {:.2f}'.format(preco - (preco /20)))
elif opc == 3:
    print('O valor a ser pago será R$ {:.2f}'.format(preco))
elif opc == 4:
    print('O valor a ser pago será R$ {:.2f}'.format((preco/ 5) + preco))
else:
    print('Sessão finalizada')
