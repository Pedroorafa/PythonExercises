#crie um programa com uma tupla de 0 a 20
#e mostre o numero digitado no teclado de 0 a 20 e mostre-o por extenso
contagem = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
numero = int(input('Digite um número: '))
escolhido = contagem[numero]
print(f'o número digitado foi {escolhido}')
