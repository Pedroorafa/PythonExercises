from datetime import date
def voto(a):
    b = (date.today().year - a)
    if 16 > b:
        r = ('Você não pode votar.')
    elif 16 <= b < 18 or b > 65:
        r = ('Voto Opcional.')
    else:
        r = ('Voto Obrigatório.')
    print(f'Você tem {b} anos: {r}')

a = int(input('Qual o seu ano de nascimento? '))
voto(a)
