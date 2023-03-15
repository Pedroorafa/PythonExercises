def area(l, c):
    print('-'*20)
    print(f'A área de um terreno {l}x{c} é de {l*c}m²')


print('Controle de terreno')
print('-'*20)
largura = float(input('Digite a largura em metros do terreno: '))
comprimento = float(input('Digite o comprimento em metros do terreno: '))
area(largura, comprimento)
