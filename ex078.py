#faça um programa que leia 5 valores numericos e guarde na lista
#mostre qual foi o maior e o menor e suas respectivas posições na lista
valores = list()
for cont in range(0,5):
    valores.append(int(input(f'Digite um valor para a posição {cont}: ')))
print(f'Os valores digitados foram {valores}')
print(f'O maior valor digitado foi {max(valores)} nas posições ', end='')
for p, v in enumerate(valores):
    if v == max(valores):
        print(f'{p}...', end='')
print()
print(f'O menor valor digitado foi {min(valores)} nas posições ', end='')
for p, v in enumerate(valores):
    if v == min(valores):
        print(f'{p}...', end='')
print()
