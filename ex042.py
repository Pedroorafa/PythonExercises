#refaça exercicio 035 e diga
#se o triangulo é Equilátero, isóceles ou escaleno
r1 = float(input('Escreva o valor da primera reta: '))
r2 = float(input('Escreva o valor da segunda reta: '))
r3 = float(input('Escreva o valor da terceira reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('É possivel fazer um triângulo com essas retas')
    if r1 == r2 == r3:
        print('Esse triângulo é equilátero')
    elif r1 == r2 or r1 == r3 or r3 == r2:
        print('Esse triângulo é isóceles')
    else:
        print('Esse triangulo é escaleno')
else:
    print('Não é possivel fazer um triângulo com essas retas')
