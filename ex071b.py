nota50 = nota20 = nota10 = nota1 = 0
valorsaque = int(input('Qual será o valor a ser sacado? '))
nota50 = valorsaque // 50
print(f'{nota50} notas de R$50')
nota20 = (valorsaque % 50) // 20
print(f'{nota20} notas de R$20')
nota10 = ((valorsaque % 50) % 20) // 10
print(f'{nota10} notas de R$10')
nota1 = (((valorsaque % 50) % 20) % 10) // 1
print(f'{nota1} notas de R$1')