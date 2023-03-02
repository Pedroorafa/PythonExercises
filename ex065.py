#crie um programa que leia varios numeros
#ao final do programa fale a média dos numeros e qual foi o maior e o menor
#o programa deve perguntar se vc quer continuar ou terminar
c = 1
s = t = maior = menor = media = 0
while c != 0:
    n = int(input('Digite um número: '))
    t = t + 1
    s += n
    if t == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    c = int(input('Deseja continuar? [ 1 ] SIM, [ 0 ] NÃO: '))
    while c != 1 and c != 0:
        c = int(input('Erro de digitação, Deseja continuar? [ 1 ] SIM, [ 0 ] NÃO: '))
media = s / t
print('O total de números digitados foi {}, a soma deles deu {} a média {} o maior número foi {} e o menor {}'.format(t, s, media, maior, menor))


