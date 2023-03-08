lista = [[] for i in range(2)]
r = 3
for c in range(0, 7):
    n = int(input(f'Digite o {c+1}º valor: '))
    if c == 0:
        lista[0].append(n)
        if n % 2 == 0:
            r = 1
        else:
            r = 0
    elif n % 2 == 0:
        if r == 1:
            lista[0].append(n)
        else:
            lista[1].append(n)
    else:
        if r == 1:
            lista[1].append(n)
print(sorted(lista[0]))
print(sorted(lista[1]))
