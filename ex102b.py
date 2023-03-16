def fatorial(n, show=False):
    """
    -> Calcula o fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (Opcional) mostra a conta.
    :return: O valore fatorial de n.
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(f'{c}', end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    print(f)


fatorial(5, True)