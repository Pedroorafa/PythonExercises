lista = str(input('Digite sua expressão: '))
cont = []
for simb in lista:
    if simb == '(':
        cont.append('(')
    elif simb == ')':
        if len(cont) > 0:
            cont.pop()
        else:
            cont.append(')')
            break
if len(cont) == 0:
    print('Sua expressão está certa')
else:
    print('Sua expressão está errada')
