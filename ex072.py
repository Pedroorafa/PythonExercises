#crie um programa com uma tupla de 0 a 20
#e mostre o numero digitado no teclado de 0 a 20 e mostre-o por extenso
contagem = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
            'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezesseis', 'dezessete',
            'dezoito', 'dezenove', 'vinte')
while True:
    numero = int(input('Digite um número 0 á 20: '))
    if 0 <= numero <= 20:
        break
    print('Tente novamente')
escolhido = contagem[numero]
print(f'o número digitado foi {escolhido}')
