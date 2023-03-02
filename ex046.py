#faça um programa que execute uma contagem regressiva na tela para estourar fogos de artificio
#10 até 0 com uma pausa de 1seg entre eles
from time import sleep
for c in range(10, -1, -1):
    sleep(0.5)
    print(c)
print('BUMMM ~le folgos de artifícios~')
