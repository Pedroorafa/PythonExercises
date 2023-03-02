from random import randint
from emoji import emojize
from time import sleep
pc = randint(0, 5)
print('-===-===-'*20)
print('Tente adivinhar em qual número estou pensando')
print('-===-===-'*20)
j = int(input('Em qual número eu pensei: '))
print('Prosessando...')
sleep(2)
if pc == j:
    print(emojize('Parabéns! Você acertou!:laughing:', language= 'alias'))
else:
    print(emojize('Que pena, você errou!:disappointed:', language= 'alias'))
