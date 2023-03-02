#leia o ano de nasciemento e veja se ele ainda vai se alistar, se é hora de se alistar ou se já passou
#quanto tempo falta ou quanto tempo passou do prazo
from datetime import date
nasc = int(input('Em que ano voê nasceu? '))
tempo = (date.today().year - nasc)
if tempo < 18:
    print('Ainda falta {} anos para você se alistar'.format(18 - tempo))
elif tempo == 18:
    print('Está na hora de você se alistar')
else:
    print('Já passou {} anos do seu alistamento'.format(tempo - 18))
