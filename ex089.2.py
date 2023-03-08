lista = list()
while True:
    nome = str(input('Nome: '))
    n1 = int(input('Nota 1: '))
    n2 = int(input('Nota 2: '))
    media = (n1 + n2) / 2
    lista.append([nome, [n1, n2], media])
    r = str(input('Ques continuar? [S/N] '))
    if r in 'Nn':
        break

print('-='*50)
print(f'{"Nº":<4} {"NOME":<10} {"MÉDIA":>4}')
print('-'*50)

for i, l in enumerate(lista):
    print(f'{i:<4}{l[0]:<10}{l[2]:>4.2f}')
print('-'*50)
while True:
    op = int(input('Mostrar nota de qual aluno? [999 para interromper] '))
    if op == 999:
        break
    if op <= len(lista)-1:
        print(f'A nota de {lista[op][0]} são {lista[op][1]}')
        print('-' * 50)
print('<<<<<<<<VOLTE SEMPRE>>>>>>>>>')
