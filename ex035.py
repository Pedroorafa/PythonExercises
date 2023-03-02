#desenvolva um programa que leia o comprimento de 3 retas e diga se pode ou não formar um triangulo
r1 = float(input('Escreva o valor da primera reta: '))
r2 = float(input('Escreva o valor da segunda reta: '))
r3 = float(input('Escreva o valor da terceira reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('É possivel fazer um triângulo com essas retas')
else:
    print('Não é possivel fazer um triângulo com essas retas')
