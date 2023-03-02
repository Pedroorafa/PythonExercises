#faça um programa que leia o ano e fale se ele é bissexto
from datetime import date
a = int(input('Qual ano você quer analizar? Digite 0 se for o ano atual '))
if a == 0:
    a = date.today().year
if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    print('O ano {} é bissexto'.format(a))
else:
    print('O ano {} não é bissexto'.format(a))
