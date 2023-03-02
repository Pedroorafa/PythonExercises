#leia nome de pessoa e diga se tem SILVA no nome
n = str((input('Digite um nome ')).strip())
r = (n.upper().find('SILVA'))
if r>-1:
    print('Essa pessoa tem SILVA no nome')
if r==-1:
    print('Essa pessoa não tem SILVA no nome')
