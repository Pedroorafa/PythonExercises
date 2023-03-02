#crie um programa que leia varios numeros inteiros pelo teclado
#o programa so vai parar quando digitar 999
#mostre quantos numeros foram digitados e a soma deles desconsiderando o 999
c = soma = n = 0
print('Digite os números a serem somado ou digite 999 para finalizar')
n = int(input('Digite o número: '))
while n != 999:
    soma = soma + n
    c += 1
    n = int(input('Digite o número: '))
print('Foram digitados {} números e a soma total deles deu {}'.format(c, soma))
