lista = list()
alunodados = list()
notadados = list()

while True:
    nome = str(input('Nome: '))
    n1 = int(input('Nota 1: '))
    n2 = int(input('Nota 2: '))
    alunodados.append(nome)
    notadados.append(n1)
    notadados.append(n2)
    alunodados.append(notadados[:])
    lista.append(alunodados[:])
    alunodados.clear()
    notadados.clear()
    r = str(input('Ques continuar? [S/N] '))
    if r in 'Nn':
        break

print('-='*50)
print(f'{"Nº":<4} {"NOME":<5} {"MÉDIA":>20}')
print('-'*50)
c = 0
for i in lista:
    print(f'{c:<4} {lista[c][0]:<15}', end='')
    print(f'{(lista[c][1][0] + lista[c][1][1]) / 2:>20.1f}')
    c += 1
print('-'*50)
while True:
    nota = int(input('Mostrar nota de qual aluno? [999 para interromper] '))
    if nota == 999:
        break
    print(f'A nota de {lista[nota][0]} são {lista[nota][1]}')
    print('-' * 50)



