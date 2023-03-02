#escreva um programa  que calcule o salario de um funcionario e escreva seu aumento
#para salarios superiores a R$1.250,00, calcule um aumento de 10%
#para salários menores o aumento será de 15%
import math
s = float(input('Escreva seu salário: '))
if s > 1250:
    print('O seu salário vai aumentar para: R${}'.format(s+(s*10/100)))
else:
    print('O seu salário vai aumentor para: R${}'.format(s+(s*15/100)))

