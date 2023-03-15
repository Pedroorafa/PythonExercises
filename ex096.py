def area():
    print('-'*20)
    print(f'A área de um terreno {l}x{c} é de {l*c}m²')


print('Controle de terreno')
print('-'*20)
l = float(input('Digite a largura em metros do terreno: '))
c = float(input('Digite o comprimento em metros do terreno: '))
area()