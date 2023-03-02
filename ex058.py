#melhore o ex028, o pc vai pensar em um numeor de 0 a 10 e o jogador vai ter quantas chances forem necessarias
#depois apresente quantas chances foram necessarias para acertar
from random import randint
from emoji import emojize
from time import sleep
pc = randint(1, 10)
print('-===-===-'*20)
print('Tente adivinhar em qual número estou pensando')
print('-===-===-'*20)
j = int(input('Em qual número estou pensando? '))
print('Prosessando...')
sleep(2)
while pc != j:
    print(emojize('Que pena, você errou!:disappointed:', language='alias'))
    if pc > j:
        print('O número pensado foi um pouco maior...')
    else:
        print('O número pensado foi um pouco menor...')
    j = int(input('Tente novamente! Em qual número estou pensando? '))
    print('Prosessando...')
    sleep(2)
print(emojize('Parabéns! Você acertou!:laughing:', language= 'alias'))
