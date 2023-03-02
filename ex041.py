#confederação de natação precida de um programa que leia o ano de nascimento de atras e informe a categoria
#<9 mirim
#<14 infantil
#<19 junior
#<20 sênior
#>20 master
from datetime import date
nasc = int(input('Imforme a data de nascimento do atleta: '))
idade = date.today().year - nasc
if idade <=9:
    print('Atleta classificado como MIRIM')
elif 9< idade <=14:
    print('Atleta classificado como INFANTIL')
elif 14< idade <=19:
    print('Atleta classificado como JUNIOR')
elif idade == 20:
    print('Atleta classificado como SÊNIOR')
else:
    print('Atleta classificado como MASTER')
