#crie um tupla com os 20 primeiros colocados do campeonato brasileiro de fut em ordem
#a - mostre os 5 primeiros colocados
#b - os ultimos 4 colocados
#c - uma lista com o time em ordem alfabetica
#d - em que colocação esta o time da chapecoense
times = 'América-MG', 'Athletico-Pr', 'Atlético-MG', 'Bahia', 'Botafogo', 'Bragantino', 'Corinthians', 'Coritiba', 'Cruzeiro', 'Cuiabá', 'Flamengo', 'Fluminense', 'Fortaleza', 'Goiás', 'Gremio', 'Internacional', 'Palmeiras', 'Santos', 'Vasco'
print(f'Classificação dos {len(times)+ 1} primeiros times do Campeonato Brasileiro Série A')
print(f'Os 5 primeiros colocados são {times[0:5]}')
print(f'Os quatro ultimos colocados foram {times[-4:]}')
print('Segue a baixo a lista em ordem alfabética: ')
print(sorted(times))
