#leia duas notas, calcule a média e fala se foi aprovado, recuperação ou reprovado
#<5 reprovado; 5<?<7 recuperação; 7< aprovado
n1 = float(input('Digite sua nota na prova: '))
n2 = float(input('Digite sua nota na outra prova: '))
m = (n1 + n2) / 2
if m < 50:
    print('Você reprovou')
elif 40 < m < 70:
    print('Você está de recuperação')
else:
    print('Você foi aprovado')
