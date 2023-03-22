def notas(*n, sit=False):
    """
    -> Função para analizar as notas e situação de cada aluno
    :param n: Uma ou mais notas do aluno
    :param sit: Mostra ou não a situação do aluno
    :return: Retorna o valor correspondente
    """
    r = dict()
    r['Total'] = len(n)
    r['Maior'] = max(n)
    r['Menor'] = min(n)
    r['Média'] = sum(n) / len(n)
    if sit:
        if 50 <= r['Média'] < 70:
            r['Situação'] = 'Razoável'
        elif r['Média'] >= 70:
            r['Situação'] = 'Boa'
        else:
            r['Situação'] = 'Ruim'

    return r


resp = notas(80, 78, 50, 80, 55, sit=True)
print(resp)
help(notas)