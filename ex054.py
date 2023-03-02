#leia a data de nascimento de 7 pessoas e mostre quantas não atingiram a maioridade (21 anos)
from datetime import date
s = 0
for c in range(1, 4):
    n = int(input('Em que ano você nasceu? '))
    if (date.today().year - n) < 20:
        s += 1
if s == 0:
    print('Todas as pessoas atingiram a maioridade')
else:
    print('{} dessas pessoas não atingiram a maioridade'.format(s))


