cadastro = dict
def jogo(jog='<desconhecido>', gol=0):
    print(f'O jogador {jog} fez {gol} gol(s)')


j = str(input('Digite o nome do jogador: '))
g = str(input('Digite o número de gols '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if j.strip() == '':
    jogo(gol=g)
else:
    jogo(j, g)
