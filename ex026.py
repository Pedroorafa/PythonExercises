#Leia um frase e diga:
#quantas vezes aparece o A
#em que posição aparece a primeira vez
#em que posição aparece a ultima
f = str(input('Digite um frase: ')).upper().strip()
v = (f.count('A'))
print('A letra A aparece {} vezes nesta frase.'.format(v))
if v>0:
    print('A letra A aparece a primeira vez na posição {}'.format(f.find('A')+1))
    print('A letra A aparece pela última vez na posição {}'.format(f.rfind('A')+1))





