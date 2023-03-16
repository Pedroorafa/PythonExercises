def fatorial(n, show=False):
    """
    -> Calcula o fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (Opcional) mostra a conta.
    :return: O valore fatorial de n.
    """
    c = (n - 1)
    r = n
    if show == True:
        print(f'{n}', end='')
    while c > 0:
        r = (r * c)
        if show == True:
            print(f' x {c}', end='')
        c -= 1
    if show == True:
        print(f' = {r}')
    else:
        print(r)


fatorial(5)
help(fatorial)
