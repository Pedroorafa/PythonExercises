#crie 5 números aleatórios e os coloque em uma tupla
#mostre a listagem dos números gerados
#e qual foi o menor e o maoir
from random import randint
num = randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100)
print('Os valores sorteados foram: ', end='')
for n in num:
    print(f'{n} ', end='')
print(f'\nO maior número digitado foi {max(num)}')
print(f'O menor número digitado foi {min(num)}')
