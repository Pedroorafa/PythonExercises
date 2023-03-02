#escreva um programa que vai aprovar um empréstimo para compra de uma casa
#O programa vai perguntar o valor da casa
#o salário do comprador
#e em quantos anos ele vai pagar
#calcule o valor da prestação, sabendo que ela não pode exceder o o valor de 30% do salário, senão será negada
casa = float(input('Qual o valor da casa que você quer compara? '))
salario = float(input('Qual o seu salário? '))
tempo = int(input('Quantos anos de finânciamento? '))
if (casa / tempo) <= (salario / 10)*3:
    print('Parabéns! seu empréstimo foi aprovado,o valor de cada parcela será R$ {:.2f}'.format (casa / tempo))
else:
    print('Seu empréstimo foi reprovado')
