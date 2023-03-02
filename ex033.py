#faça um programa que leia tres numeros e fale qual é o maior e qual é o menor
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite outro número: '))
if n2<n1>n3:
    print('{} é o maior dos números digitados'.format(n1))
    if n1>n2<n3:
        print('e {} é o menor'.format(n2))
    else:
        print('e {} é o menor'.format(n3))
elif n1<n2>n3:
    print('{} é o maior dos números digitados'.format(n2))
    if n2>n1<n3:
        print('e {} é o menor'.format(n1))
    else:
        print('e {} é o menor'.format(n3))
else:
    print('{} é o maior dos números digitados'.format(n3))
    if n3>n1<n2:
        print('e {} é o menor'.format(n1))
    else:
        print('e {} é o menor'.format(n2))
