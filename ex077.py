#crie uma tupla com várias palavras sem acento
#mostrar para cada palavra, quais são as suas vogais
palavras = 'oi', 'ola', 'bom', 'acabou'
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos: ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end='')