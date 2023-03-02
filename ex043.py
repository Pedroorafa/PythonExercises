#leia o imc e diga se o status
#<18.5 abaixo do peso, 18.5 a 25 peso ideal, 25 a 30 sobre peso, 30 a 40 obesidade e acima de 40 obesidade morbida
a = float(input('Insira a sua altura: '))
p = float(input('Insira o seu peso: '))
imc = p / (a ** 2)
print(imc)
if imc < 18.5:
    print('Você está a baixo do peso')
elif 18.5 <= imc < 25:
    print('Você está no peso ideal')
elif 25 <= imc < 30:
    print('Você está com sobrepeso')
elif 30 <= imc < 40:
    print('Você está obeso(a)')
else:
    print('Você esta com obesidade morbida')