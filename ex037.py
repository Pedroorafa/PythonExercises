#Leia um número inteiro e peça para o usuario escolher a conversão
#1 binario, 2 octal, 3 hexadecimal
n = int( input('Escreva um número: '))
print('Escolha uma das bases de conversão:')
print('Se escolher binário digite: 1')
print('Se escolher octal digite: 2')
print('Se escolher hexadecimal: 3')
print('Nenhuma das opções: 0')
e = int(input('Sua escolha:'))
if e == 1:
    print(bin(n)[2:])
if e == 2:
    print(oct(n)[2:])
if e == 3:
    print(hex(n)[2:])
else:
    print('Programa finalizado')
