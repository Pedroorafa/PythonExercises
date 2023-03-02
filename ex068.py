from random import randint
j = pc = s = v = 0
print('=-=*=-='*5)
print('Vamos jogar PAR ou ÍMPAR!!')
print('=-=*=-='*5)
while True:
    j = int(input('Escolha um número de 1 a 5: '))
    o = str(input('Escolhe Par[P] ou Ímpar[I]? ')).strip().upper()[0]
    while o not in 'PI':
        o = str(input('Ocorreu um erro, escolhe novamente, Par[P] ou Ímpar[I]? ')).strip().upper()[0]
    pc = randint(1, 5)
    s = j + pc
    print('~' * 13)
    print(f'Você jogou {j} e o computador {pc} total deu {s}')
    print('~' * 25)
    if o == 'P':
        print('Deu PAR')
        if s % 2 == 0:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU')
            break
    elif o == 'I':
        print('Deu ÍMPAR')
        if s % 2 == 1:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU')
            break
    print('Vamor jogar novamente')
print(f'GAME OVER !!! você venceu {v} vezes')
