#mostre a soma de todos os número impares multiplos de 3 que se encontram entro 1-500
s = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        s += c
print(s)
