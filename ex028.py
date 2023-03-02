#faça o pc pensar em um numero de 0 a 5
#peça para o usuario tentar descobrir o numero
#o programa deve escrever na tela se o usuario ganhou ou perdeu
from random import choice
import emoji
print('A máquina está pensando em um número...')
n = [0, 1, 2, 3, 4, 5]
pc = choice(n)
user = int(input('Tente acertar qual número a maquina esta pensando: '))
print('O número escolhido foi {}'.format(pc))
if user == pc:
    print(emoji.emojize('Parabéns! Você acertou!:laughing:', language='alias'))
else:
    print(emoji.emojize('Que pena! Você errou!:disappointed:', language='alias'))








