#leia um nome de cidade e diga se começa ou não com SANTO
c = str((input('Escreva o nome da cidade: ')).strip())
r = (c.upper().find('SANTO'))
if r>0 or r<0:
    print('Essa cidade não começa com SANTO')
if r==0:
    print('Essa cidade começa com SANTO')