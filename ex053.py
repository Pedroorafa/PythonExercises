#leia uma frase e diga se ela é um palíndromo, desconsiderando os espaços
#ler de frente e trás é a mesma coisa
n1 = str(input('Escreva uma palavra: ')).strip()
n2 = n1.split()
n3 =''.join(n2)
n4 = n3 [::-1]
print(n3)
print(n4)
if n4 == n3:
    print('Essa palavra é um Palíndromo')
else:
    print('Essa palavra não é um Palíndromo')
